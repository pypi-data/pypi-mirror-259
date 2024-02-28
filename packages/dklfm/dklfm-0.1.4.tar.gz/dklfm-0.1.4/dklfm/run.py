import sys

import hydra
import numpy as np
import torch
import pytorch_lightning as pl
from omegaconf import DictConfig
from pathlib import Path
from torch.utils.data import DataLoader
from pytorch_lightning.callbacks import ModelCheckpoint, LearningRateMonitor
from pytorch_lightning.callbacks import EarlyStopping
from pytorch_lightning.loggers import TensorBoardLogger
import matplotlib.pyplot as plt

from alfi.models.mlp import MLP
from alfi.models import NeuralOperator

from dklfm.util import map_device
from dklfm.data.dataset_helpers import load_dataset
from newdklfm import DKLFM, SkipMLP


def build_submodels(cfg, dataset):
    ds_cfg = cfg[f"dataset_{cfg['training']['dataset']}"]
    block_dim = ds_cfg['block_dim']
    embedding_dim = ds_cfg['embedding_dim']

    # Embedding over the output observations
    # embedder = TransformerEncoder(output_dim, output_dim=embedding_dim, num_hidden_layers=2).type(torch.float64)
    modes = ds_cfg['modes']# 5
    width = ds_cfg['width']
    deep_kernel_dim = 32
    add_inputs = block_dim
    embedder = NeuralOperator(block_dim, 1, embedding_dim, modes, width, params=False)#.type(torch.float64)
    # embedder = MLP(data_dim, data_dim, latent_dim=8, num_hidden_layers=3)

    # Deep kernel
    nn_latent = MLP(block_dim + embedding_dim, deep_kernel_dim, latent_dim=deep_kernel_dim, num_hidden_layers=0).type(torch.float64)
    nn_output = MLP(block_dim + embedding_dim, deep_kernel_dim, latent_dim=deep_kernel_dim, num_hidden_layers=0).type(torch.float64)
    nn_common = SkipMLP(deep_kernel_dim, 32, latent_dim=deep_kernel_dim, num_hidden_layers=4).type(torch.float64)
    return embedder, [nn_common, nn_latent, nn_output], add_inputs


def evaluate(dklfm, batch, save_prefix):
    batch = [b.to(dklfm.device) for b in batch]
    with torch.no_grad():
        mu_f_y, k_f_y, _, _ = dklfm.f_given_y(batch)
        mu_f_y = mu_f_y.cpu()
        k_f_y = k_f_y.cpu()
        mu_y, _ = dklfm.ystar_given_y(batch, batch[1])
        mu_y = mu_y.cpu()
    plt.figure()
    x_cond_blocks, x_cond, y_cond, f_cond = [b.cpu() for b in batch]
    if x_cond.shape[-1] > 1:
        x_width = int(np.sqrt(y_cond.shape[-1]))

    mu_y = mu_y.reshape(y_cond.shape).detach()

    i = np.random.randint(0, mu_y.shape[0])

    if x_cond.shape[-1] == 1:
        fig, axes = plt.subplots(ncols=2)
        print(mu_y.shape)
        axes[0].plot(mu_y[i].t())
        axes[1].plot(y_cond[i].t())
        plt.savefig(f"{save_prefix}_output.pdf", bbox_inches="tight")

        plt.figure()
        plt.plot(mu_f_y.squeeze()[i].detach())
        plt.plot(f_cond[i])
        plt.savefig(f"{save_prefix}_latent.pdf", bbox_inches="tight")
    else:
        fig, axes = plt.subplots(ncols=2)
        # axes[0].imshow(mu_y_f[4].view(x_width, x_width).detach(), origin='lower')
        axes[0].imshow(mu_y[i].view(x_width, x_width).detach(), origin='lower')
        axes[1].imshow(y_cond[i].view(x_width, x_width), origin='lower')
        plt.savefig(f"{save_prefix}_output.pdf", bbox_inches="tight")

        fig, axes = plt.subplots(ncols=2)
        axes[0].imshow(mu_f_y.squeeze()[i].view(x_width, x_width).detach(), origin='lower')
        axes[1].imshow(f_cond[i].view(x_width, x_width), origin='lower')
        plt.savefig(f"{save_prefix}_latent.pdf", bbox_inches="tight")
        print("Latent MSE:", torch.square(f_cond - mu_f_y.squeeze()).squeeze().mean(-1).min())
        print("Output MSE:", torch.square(y_cond - mu_y.squeeze()).squeeze().mean(-1).min())

    with open(f"{save_prefix}_mse.txt", "w") as f:
        latent_mse = torch.square(f_cond - mu_f_y.squeeze()).mean()
        output_mse = torch.square(y_cond - mu_y.squeeze()).mean()
        f.write(f"latent_mse={str(latent_mse)};output_mse={str(output_mse)}")
        print("Latent MSE:", latent_mse)
        print("Output MSE:", output_mse)


@hydra.main(version_base=None, config_path="conf", config_name="train")
def app(cfg: DictConfig):
    # Load data
    synthetic_dataset, real_dataset, scaler_modules = load_dataset(cfg)

    print("Dataset shapes:")
    print(f"-- Output observations: {synthetic_dataset.y.shape}")
    print(f"-- Latent observations: {synthetic_dataset.f.shape}")
    print(f"-- Inputs observations: {synthetic_dataset.timepoints.shape}")

    num_epochs = cfg['training']['num_epochs']
    device = map_device(cfg['training']['device'])
    logger = TensorBoardLogger(Path(__file__).parent / "tb_logs", name=cfg['training']['dataset'])
    save_dir = Path(logger.log_dir)
    print("Save directory:", save_dir)

    batch_size = cfg['training']['batch_size']
    train_loader = DataLoader(synthetic_dataset, batch_size=batch_size, num_workers=12)
    val_loader = DataLoader(synthetic_dataset.validation(), batch_size=batch_size)

    # Instantiate the model
    if cfg['training']['load_version'] is not None:
        path = save_dir.parent / f"version_{cfg['training']['load_version']}/checkpoints/last.ckpt"
        cfg['model']['ckpt_path'] = path
    embedder, nns, add_inputs = build_submodels(cfg, synthetic_dataset)
    model = DKLFM(cfg, embedder, nns, add_inputs=add_inputs)

    # Instantiate the trainer
    log_dir = Path(logger.log_dir)
    log_dir.mkdir(exist_ok=True, parents=True)
    (log_dir / 'hydra').symlink_to(Path.cwd())
    for obj_name, obj in scaler_modules.items():
        torch.save(obj, logger.log_dir + f'/{obj_name}.pt')
    if torch.cuda.is_available():
        torch.set_float32_matmul_precision('medium')

    checkpoint_monitor = 'val_loss'
    patience = cfg['training']['patience']

    trainer = pl.Trainer(
        accelerator=device,
        log_every_n_steps=10,
        max_epochs=num_epochs,
        logger=logger,
        callbacks=[
            ModelCheckpoint(save_top_k=3, monitor=checkpoint_monitor, save_last=True),
            ModelCheckpoint(save_top_k=3, monitor="mse", save_last=True, filename="best_mse"),
            ModelCheckpoint(save_top_k=3, monitor="harmonic_mse", save_last=False, filename="best_harmonic_mse"),
            EarlyStopping(monitor=checkpoint_monitor, patience=patience),
            LearningRateMonitor(logging_interval='epoch'),
        ]
    )

    trainer.fit(model, train_dataloaders=train_loader, val_dataloaders=val_loader, ckpt_path=cfg['model']['ckpt_path'])

    (log_dir / "evaluation").mkdir()
    batch = next(iter(train_loader))
    for ckpt_file in (log_dir / 'checkpoints').glob("*.ckpt"):
        dklfm = DKLFM.load_from_checkpoint(
            ckpt_file,
            cfg=cfg, embedder=embedder, deepkernels=nns, add_inputs=add_inputs
        )
        evaluate(dklfm, batch, save_prefix=log_dir / "evaluation" / ckpt_file.stem)


if __name__ == '__main__':
    sys.argv.append('hydra.job.chdir=True')
    # load_dotenv()
    app()
