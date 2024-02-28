import sys
from pathlib import Path
from dotenv import load_dotenv

import hydra
import numpy as np
import torch
import gpytorch
from omegaconf import DictConfig
from pytorch_lightning.callbacks import ModelCheckpoint, EarlyStopping, LearningRateMonitor
from pytorch_lightning.loggers import TensorBoardLogger
import pytorch_lightning as pl
from torch.utils.data import DataLoader
from matplotlib import pyplot as plt
from torch.nn import LSTM
from alfi.models.mlp import MLP

from dklfm.model import DeepKernelLFM, DKLFMWrapper
from alfi.models import NeuralOperator
from dklfm.transformer_encoder import TransformerEncoder
from dklfm.util import map_device, Scaler
from dklfm.data.dataset_helpers import synthetic_transcriptomics, load_dataset
from dklfm.data.dklfm_dataset import DeepKernelLFMDataset

plt.rcParams['axes.unicode_minus'] = False


def get_embedder(cfg):
    ds_cfg = cfg[f"dataset_{cfg['training']['dataset']}"]
    block_dim = ds_cfg['block_dim']
    out_channels = cfg['embedder']['out_channels']

    if cfg['embedder']['type'] == 'lstm':
        embedder_model = LSTM(1, out_channels, 1, batch_first=True, bidirectional=False).type(
            torch.float64)  # input_size, hidden_size, num_layers

        def embedder(y_reshaped, **kwargs):
            _, (hn, _) = embedder_model(y_reshaped)
            return hn
    elif cfg['embedder']['type'] == 'transformer':
        embedder_model = TransformerEncoder(ds_cfg['embedder_in_channels'], output_dim=out_channels).type(torch.float64)
        def embedder(y_reshaped, x_cond=None, **kwargs):
            if cfg['training']['dataset'] == 'reactiondiffusion':
                n_task = y_reshaped.shape[0]
                y_reshaped = y_reshaped.view(n_task, -1, 1)
                # x_cond = x_cond.view(n_task, -1, 2)
                # y_reshaped = torch.cat([x_cond, y_reshaped], dim=-1)
            hn = embedder_model(y_reshaped).mean(dim=1)

            return hn

    else:
        embedder_model = NeuralOperator(
            block_dim,
            ds_cfg['embedder_in_channels'],
            out_channels,
            ds_cfg['modes'],
            cfg['embedder']['width'],
            params=False
        )

        def embedder(y_reshaped, x_cond=None):
            if cfg['training']['dataset'] == 'reactiondiffusion':
                n_task = y_reshaped.shape[0]
                y_reshaped = y_reshaped.view(n_task, ds_cfg['t_width'], ds_cfg['x_width'], 1)
                # x_cond = x_cond.view(n_task, ds_cfg['t_width'], ds_cfg['x_width'], 2)
                # y_reshaped = torch.cat([x_cond, y_reshaped], dim=-1)

            hn = embedder_model(y_reshaped.type(torch.float32)).mean(1).type(torch.float64)

            if cfg['training']['dataset'] == 'reactiondiffusion':
                hn = hn.std(1)

            return hn
    return embedder_model, embedder


def get_model(cfg, synthetic_dataset, scaler_modules):
    ds_cfg = cfg[f"dataset_{cfg['training']['dataset']}"]
    block_dim = ds_cfg['block_dim']
    out_channels = cfg['embedder']['out_channels']
    latent_dims = cfg['model']['latent_dims']
    num_hidden_layers = ds_cfg['num_hidden_layers']
    include_embedding = cfg['model']['include_embedding']
    ckpt_path = cfg['model']['ckpt_path']

    if include_embedding is not False:
        embedder_model, embedder_fn = get_embedder(cfg)
    if cfg['model']['fixed_noise']:
        likelihood = gpytorch.likelihoods.FixedNoiseGaussianLikelihood(
            torch.ones(1, dtype=torch.float64) * ds_cfg['initial_noise']).type(torch.float64)
        likelihood_f = gpytorch.likelihoods.FixedNoiseGaussianLikelihood(
            torch.ones(1, dtype=torch.float64) * ds_cfg['initial_noise']).type(torch.float64)
    else:
        from gpytorch.constraints import LessThan
        likelihood_f = gpytorch.likelihoods.GaussianLikelihood(noise_constraint=LessThan(1.1*ds_cfg['initial_noise'])).type(torch.float64)
        likelihood_f.noise = ds_cfg['initial_noise']
        likelihood = gpytorch.likelihoods.GaussianLikelihood(noise_constraint=LessThan(1.1*ds_cfg['initial_noise'])).type(torch.float64)
        likelihood.noise = ds_cfg['initial_noise']

    joint_operator = MLP(block_dim + out_channels, latent_dims, num_hidden_layers).type(torch.float64)
    x1_operator = MLP(1 + out_channels, latent_dims, num_hidden_layers).type(torch.float64)
    x2_operator = MLP(1 + out_channels, latent_dims, num_hidden_layers).type(torch.float64)

    model = DeepKernelLFM(
        synthetic_dataset.train_x_cond_blocks, synthetic_dataset.train_y_cond, synthetic_dataset.train_f_cond,
        likelihood, likelihood_f,
        joint_operator if include_embedding is not False else (x1_operator, x2_operator),
        num_functions=synthetic_dataset.y.shape[1],
        embedder=(embedder_model, embedder_fn) if include_embedding is not False else None,
        kernel=cfg['model']['kernel'],
        kernel_in_dims=latent_dims,
        include_embedding=include_embedding
    )
    # model.covar_module = model.covar_module.type(torch.float64)
    model.covar_module.base_kernel.lengthscale *= 0
    model.covar_module.base_kernel.lengthscale += cfg['model']['lengthscale']
    if cfg['model']['kernel'] == 'periodic':
        model.covar_module.base_kernel.period_length *= 0
        model.covar_module.base_kernel.period_length += cfg['model']['period']
    print(dict(model.named_parameters()).keys())

    # lr = 1e-4
    if ckpt_path is not None:
        return DKLFMWrapper.load_from_checkpoint(ckpt_path, cfg=cfg, model=model, mse_data=synthetic_dataset, scaler_modules=scaler_modules)
    return DKLFMWrapper(cfg, model, mse_data=synthetic_dataset, scaler_modules=scaler_modules)


@hydra.main(version_base=None, config_path="conf", config_name="train")
def app(cfg: DictConfig):
    num_epochs = cfg['training']['num_epochs']
    device = map_device(cfg['training']['device'])
    logger = TensorBoardLogger(Path(__file__).parent / "tb_logs", name=cfg['training']['dataset'])
    save_dir = Path(logger.log_dir)
    print("Save directory:", save_dir)

    # Load data
    synthetic_dataset, real_dataset, modules_to_save = load_dataset(cfg)
    batch_size = cfg['training']['batch_size']
    train_loader = DataLoader(synthetic_dataset, batch_size=batch_size)
    val_loader = DataLoader(synthetic_dataset.validation(), batch_size=batch_size)

    # Instantiate the model
    if cfg['training']['load_version'] is not None:
        path = save_dir.parent / f"version_{cfg['training']['load_version']}/checkpoints/last.ckpt"
        cfg['model']['ckpt_path'] = path
    model = get_model(cfg, synthetic_dataset, modules_to_save)

    # Instantiate the trainer

    Path(logger.log_dir).mkdir(exist_ok=True, parents=True)
    Path(logger.log_dir + '/hydra').symlink_to(Path.cwd())
    for obj_name, obj in modules_to_save.items():
        torch.save(obj, logger.log_dir + f'/{obj_name}.pt')
    if torch.cuda.is_available():
        torch.set_float32_matmul_precision('medium')
    # checkpoint_monitor = 'val_loss' if len(test_loader) > 0 else 'train_loss'
    checkpoint_monitor = 'train_loss'
    latent_mses = list()
    output_mses = list()

    trainer = pl.Trainer(
        logger=logger, log_every_n_steps=10,
        max_epochs=num_epochs,
        # gradient_clip_val=0.5,
        accelerator=device,
        callbacks=[
            ModelCheckpoint(save_top_k=1, monitor=checkpoint_monitor, save_last=True),
            EarlyStopping(monitor=checkpoint_monitor, patience=cfg['training']['patience']),
            LearningRateMonitor(logging_interval='epoch'),
        ]
    )
    trainer.fit(model, train_dataloaders=train_loader, val_dataloaders=val_loader, ckpt_path=cfg['model']['ckpt_path'])


if __name__ == '__main__':
    sys.argv.append('hydra.job.chdir=True')
    load_dotenv()
    app()
