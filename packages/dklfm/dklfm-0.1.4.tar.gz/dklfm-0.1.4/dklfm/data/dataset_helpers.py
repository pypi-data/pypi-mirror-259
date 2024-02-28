import numpy as np
import torch

from tqdm import trange
from matplotlib import pyplot as plt
from alfi.datasets import ToyTranscriptomics, ToyTranscriptomicGenerator, P53Data
from alfi.utilities.torch import spline_interpolate_gradient, softplus

from dklfm.util import Scaler
from dklfm.data.dklfm_dataset import DeepKernelLFMDataset
from dklfm import data_dir, sc_rna_dir



# input given as (batch, seq, feature)
def load_dataset(cfg, scaler_dir=None):
    dataset = cfg['training']['dataset']
    ds_cfg = cfg[f'dataset_{dataset}']

    # Scaler uses the final dimension, i.e. the times
    if scaler_dir is not None:
        y_scaler = torch.load(scaler_dir / 'y_scaler.pt')
        f_scaler = torch.load(scaler_dir / 'f_scaler.pt')
        real_y_scaler = torch.load(scaler_dir / 'real_y_scaler.pt')
        real_f_scaler = torch.load(scaler_dir / 'real_f_scaler.pt')
    else:
        y_scaler = Scaler()
        f_scaler = Scaler()
        real_y_scaler = Scaler()
        real_f_scaler = Scaler()

    y_scaler.do_scale = cfg['training']['scale_data']
    f_scaler.do_scale = cfg['training']['scale_data']
    real_y_scaler.do_scale = cfg['training']['scale_data']
    real_f_scaler.do_scale = cfg['training']['scale_data']

    if dataset == 'transcriptomics':
        synthetic_dataset = synthetic_transcriptomics(
            data_dir=sc_rna_dir, load=True,
            scalers=(y_scaler, f_scaler),
            scale_x_max=cfg['training']['scale_x_max'],
            n_training_instances=ds_cfg['n_training_tasks'],
            n_test_instances=ds_cfg['n_test_tasks']
        )
        real_dataset= None
        # real_dataset = p53_transcriptomics(data_dir='/media/jacob/ultra/genomics/microarray', t_scale=9 / 12,
        #                                    scalers=(real_y_scaler, real_f_scaler), scale_x_max=cfg['training']['scale_x_max'])
    elif dataset == 'reactiondiffusion':
        from pathlib import Path
        ultra_dir = Path("/Volumes/ultra")
        ultra_dir = Path("/media/jacob/ultra")
        # ultra_dir = Path("/Users/jacob/data")

        synthetic_spatial = torch.load(ultra_dir / 'toydata.pt')
        data = synthetic_spatial['orig_data']
        print(data.shape)
        # plt.imshow(data[0, 0].reshape(41, 41).t(), origin='lower')
        # plt.figure()
        # plt.imshow(data[0, 1].reshape(41, 41).t(), origin='lower')
        y = data[:500, 1:2].view(500, 1, 41, 41)[..., ::2, ::2].reshape(500, 1, -1).type(torch.float64)
        f = data[:500, 0:1].view(500, 1, 41, 41)[..., ::2, ::2].reshape(500, 1, -1).type(torch.float64)

        y = y_scaler.scale(y)
        f = f_scaler.scale(f)
        # plt.figure()
        # plt.imshow(y[0, 0].reshape(21, 21).t(), origin='lower')
        x = synthetic_spatial['x_observed'].view(2, 41, 41)[..., ::2, ::2].reshape(2, -1).t().type(torch.float64)
        data = None
        synthetic_spatial = None
        # n_data = n_times
        # train_indices = np.sort(np.random.permutation(np.arange(41))[:n_times])
        # print(train_indices)
        synthetic_dataset = DeepKernelLFMDataset(
            x, y, f=f, n_train=f.shape[-1], scale_x_max=cfg['training']['scale_x_max'],
            n_training_instances=ds_cfg['n_training_tasks'],
            n_test_instances=ds_cfg['n_test_tasks']
        )
        synthetic_dataset.input_dim = 2
        real_dataset = None
        # orig_data = data
        # x_observed = synthetic_spatial['x_observed']
        # num_data = 400
        # num_outputs = 1
        # num_discretised = 40
        #
        # tx = x_observed.t()[:, 0:2]
        # t_sorted = np.argsort(tx[:, 0], kind='mergesort')
        # x_observed = x_observed[:, t_sorted]
        # orig_data = torch.cat([
        #     x_observed.unsqueeze(0).repeat(num_data, 1, 1),
        #     orig_data[:num_data, :, t_sorted]
        # ], dim=1)
        # params = synthetic_spatial['params'][:num_data]
        # neural_dataset = generate_neural_dataset_2d(orig_data, params, 300, 100)
        # print(neural_dataset[0][0][0].shape)
    elif dataset == 'lotkavolterra':
        from alfi.datasets import DeterministicLotkaVolterra
        load_lokta = True
        if load_lokta:
            t, lf, y = torch.load(data_dir / 'lotka_data.pt')
        else:
            t = None
            lf = list()
            y = list()
            for _ in trange(500):
                data = DeterministicLotkaVolterra(
                    alpha = np.random.uniform(0.5, 1.),
                    beta = np.random.uniform(1., 1.4),
                    gamma = 1.,
                    delta = 1.,
                    steps=30,
                    end_time=30,
                    fixed_initial=0.8,
                    silent=True
                )
                t = data.data[0][0]
                lf.append(data.prey[::data.num_disc+1])
                y.append(data.data[0][1])

            y = torch.stack(y).unsqueeze(1)
            lf = torch.stack(lf).unsqueeze(1)
            torch.save([t, lf, y], 'lotka_data.pt')
            x_min, x_max = min(data.times), max(data.times)
            plt.plot(data.data[0][0], data.data[0][1], c='red', label='predator')
            plt.plot(torch.linspace(x_min, x_max, data.prey.shape[0]), data.prey, c='blue', label='prey')
            plt.legend()

        y = y_scaler.scale(y)
        lf = f_scaler.scale(lf)
        synthetic_dataset = DeepKernelLFMDataset(
            t, y, f=lf,
            train_indices=np.arange(0, t.shape[0]),
            scale_x_max=cfg['training']['scale_x_max'],
            n_test_instances=ds_cfg['n_test_tasks'],
        )
        real_dataset = None
    else:
        raise ValueError(f'Unknown dataset {dataset}')
    return synthetic_dataset, real_dataset, {'y_scaler': y_scaler, 'f_scaler': f_scaler, 'real_y_scaler': real_y_scaler, 'real_f_scaler': real_f_scaler}


def synthetic_transcriptomics(load=True, data_dir='../../../data', num_genes=5, num_tfs=1, scalers=None, scale_x_max=False, n_training_instances=500, n_test_instances=1.):
    if load:
        toy_dataset = ToyTranscriptomics(data_dir=data_dir)
    else:
        toy_dataset = ToyTranscriptomicGenerator(
            num_outputs=num_genes, num_latents=num_tfs, num_times=10, softplus=True, latent_data_present=True)
        toy_dataset.generate(500, 100, '../../../data/')

    num_tasks = len(toy_dataset.train_data) + len(toy_dataset.test_data)
    y = torch.from_numpy(np.stack([
        [*toy_dataset.train_data, *toy_dataset.test_data][i][0] for i in range(num_tasks)
    ])).permute(0, 2, 1)
    f = torch.from_numpy(np.stack([
        [*toy_dataset.train_data, *toy_dataset.test_data][i][1] for i in range(num_tasks)
    ])).permute(0, 2, 1)
    timepoints = y[0, 0].type(torch.float64)
    y = y[:, 1:]
    f = softplus(f)
    if scalers:
        y_scaler, f_scaler = scalers
        y = y_scaler.scale(y).type(torch.float64)
        f = f_scaler.scale(f).type(torch.float64)

    if scale_x_max:
        timepoints = timepoints / timepoints.max()
    synth_trans_dataset = DeepKernelLFMDataset(
        timepoints, y, f,
        n_train=9, n_training_instances=n_training_instances, n_test_instances=n_test_instances
    )
    return synth_trans_dataset


def p53_transcriptomics(t_scale=1.0, data_dir='../../alfi/data', scalers=None, scale_x_max=False):
    real_dataset = P53Data(data_dir=data_dir)
    y = real_dataset.m_observed.type(torch.float64)
    f = real_dataset.f_observed.repeat(3, 1, 1).type(torch.float64)
    t = real_dataset.t_observed * t_scale
    _, y, _, _ = spline_interpolate_gradient(t, y.transpose(-2, -1), num_disc=2)
    t, f, _, _ = spline_interpolate_gradient(t, f.transpose(-2, -1), num_disc=2)
    y = y.transpose(-2, -1)
    f = f.transpose(-2, -1)
    if scalers:
        y_scaler, f_scaler = scalers
        y = y_scaler.scale(y).type(torch.float64)
        f = f_scaler.scale(f).type(torch.float64)
    if scale_x_max:
        t = t / t.max()
    return DeepKernelLFMDataset(t, y, f, n_train=10)


