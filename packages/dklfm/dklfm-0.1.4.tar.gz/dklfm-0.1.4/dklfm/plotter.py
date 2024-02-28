import numpy as np
import torch
from gpytorch.distributions import MultitaskMultivariateNormal

from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

from alfi.utilities.data import create_tx
from dklfm.newdklfm import DKLFM
from dklfm.util import Scaler
from dklfm.data.dklfm_dataset import DeepKernelLFMDataset



class DeepKernelLFMPlotter:
    def __init__(
            self, model: DKLFM, dataset: DeepKernelLFMDataset,
            t_eval, y_scaler: Scaler, f_scaler: Scaler, restrict_indices=None, compute_dists=False,

    ):
        model.eval()
        self.dataset = dataset
        self.restrict_indices = restrict_indices
        n_task = dataset.n_task if restrict_indices is None else restrict_indices.shape[0]
        self.n_task = n_task
        self.n_functions = dataset.y.shape[1]
        self.t_eval = t_eval
        self.y_scaler = y_scaler
        self.f_scaler = f_scaler
        eval_input = self.t_eval.reshape(1, -1, 1).repeat(n_task, 1, 1).type(torch.float64)
        if dataset.input_dim == 2:
            eval_input = create_tx(self.t_eval, n_task)

        # out = likelihood(model(y_reshaped, eval_input))
        x_cond, y_cond, x_cond_blocks, f_cond = dataset.x_cond, dataset.y_cond, dataset.x_cond_blocks, dataset.f_cond
        if restrict_indices is not None:
            x_cond = x_cond[restrict_indices]
            y_cond = y_cond[restrict_indices]
            x_cond_blocks = x_cond_blocks[restrict_indices]

        x_cond, y_cond, x_cond_blocks, f_cond = x_cond.to(t_eval.device), y_cond.to(t_eval.device), x_cond_blocks.to(t_eval.device), f_cond.to(t_eval.device)
        with torch.no_grad():
            batch = x_cond_blocks, x_cond, y_cond, f_cond
            self.mean, self.var = model.ystar_given_y(
                batch, eval_input)
            # self.out = MultitaskMultivariateNormal.from_batch_mvn(self.mean, task_dim=0)
            self.mean = y_scaler.inv_scale(self.mean.detach().cpu().reshape(n_task, self.n_functions, -1)).transpose(-1, -2)
            self.var = self.var.detach().cpu().diagonal(dim1=-2, dim2=-1).reshape(n_task, self.n_functions, -1).transpose(-1, -2)
            # self.var = self.out.variance.detach().cpu().reshape(n_task, self.n_functions, -1).transpose(-1, -2)

            eval_input_f = self.t_eval.reshape(1, -1, 1).repeat(n_task, 1, 1).type(torch.float64)
            if dataset.input_dim == 2:
                eval_input_f = eval_input

            self.mean_f, self.var_f, _, _ = model.f_given_y(batch, eval_input_f)
            # out_f_train = model.latent_predictive(y_reshaped, train_input_f)
            self.mean_f = f_scaler.inv_scale(self.mean_f.detach().cpu())
            self.var_f = self.var_f.detach().cpu().diagonal(dim1=-2, dim2=-1)
            # print(self.mean_f.shape, dataset.train_indices)
            # self.mean_f_train = self.mean_f[:, dataset.train_indices]
            # self.var_f_train = self.var_f[:, dataset.train_indices]

            if compute_dists:
                self.kxx = model.kxx(x_cond_blocks, x_cond_blocks).evaluate().detach().cpu()
                self.kxf = model.kxf(x_cond_blocks, x_cond).evaluate().detach().cpu()
                self.kff = model.kff(x_cond, x_cond).evaluate().detach().cpu()
            self.t_eval = self.t_eval.cpu()

    def plot_results(self, task_index=0, plot_data_y=True, plot_data_f=True, plot_dists=True, by_row=True, ylabels=['Predator', 'Prey']):
        font = {'size': 15} # 44
        import matplotlib
        matplotlib.rc('font', **font)
        timepoints_cond = self.dataset.timepoints_cond
        ncols = 4 if plot_dists else 2 if self.dataset.input_dim == 1 else 4
        nrows = 2 if plot_dists else 1
        height = 10 if plot_dists else 10 if self.dataset.input_dim == 1 else 10
        width = 4 #if by_row else 17
        dims = (height, width) if not by_row else (width, height)
        fig, axes = plt.subplots(ncols=nrows if by_row else ncols, nrows=ncols if by_row else nrows, figsize=dims)
        if by_row:
            axes = np.transpose(axes)
        y_pred = self.mean[task_index], self.var[task_index]
        f_pred = self.mean_f[task_index], self.var_f[task_index].sqrt() * 2
        orig_task_index = task_index if self.restrict_indices is None else self.restrict_indices[task_index]
        y_data = self.y_scaler.inv_scale(self.dataset.y)[orig_task_index].t().detach() if plot_data_y else None
        f_shape = (self.n_task, 1, -1)
        f_data = self.f_scaler.inv_scale(self.dataset.f)[orig_task_index].squeeze() if plot_data_f else None
        f_cond = None
        if self.dataset.f_cond is not None:
            f_cond = self.dataset.f_cond
            if self.restrict_indices is not None:
                f_cond = f_cond[self.restrict_indices]
            f_cond = self.f_scaler.inv_scale(f_cond.view(f_shape))[task_index].squeeze()
        y_cond = self.dataset.y_cond
        if self.restrict_indices is not None:
            y_cond = y_cond[self.restrict_indices]
        _train_y = self.y_scaler.inv_scale(y_cond.view(self.n_task, self.n_functions, -1))
        y_cond = _train_y[task_index]
        ax_result = axes[0] if plot_dists else axes
        plot_result = self.plot_result if self.dataset.input_dim == 1 else self.plot_result_2d
        plot_result(
            ax_result, self.t_eval,
            y_pred, f_pred,
            self.dataset.timepoints, y_data, f_data,
            timepoints_cond, y_cond=y_cond, f_cond=f_cond,
            ylabels=ylabels
        )
        if plot_dists:
            im0 = axes[1, 0].imshow(np.log(self.out.covariance_matrix[task_index].detach()))
            axes[1, 0].set_title('Output covariance')
            im1 = axes[1, 1].imshow(self.kxx[task_index])
            axes[1, 1].set_title("K(x, x)")
            im2 = axes[1, 2].imshow(self.kxf[task_index])
            axes[1, 2].set_title("K(x, f)")
            im3 = axes[1, 3].imshow(self.kff[task_index])
            axes[1, 3].set_title("K(f, f)")
            ims = [im0, im1, im2, im3]
            for i in range(4):
                divider = make_axes_locatable(axes[1, i])
                cax = divider.append_axes('right', size='5%', pad=0.05)
                fig.colorbar(ims[i], cax=cax, orientation='vertical');

    def imshow(self, ax, data, label=None, **kwargs):
        size = int(np.sqrt(data.shape[0]))
        im = ax.imshow(data.view(size, size).t(), origin='lower', **kwargs)
        ax.set_title(label)
        ax.set_xlabel('time')
        ax.set_ylabel('space')
        return im

    def plot_result_2d(self, axes, t_pred, y_pred, f_pred, t_data, y_data=None, f_data=None, t_cond=None, y_cond=None, f_cond=None, ylabels=None):
        y_pred_mean, y_pred_var = y_pred
        f_pred_mean, f_pred_var = f_pred

        extent = [t_pred[0], t_pred[-1], t_pred[0], t_pred[-1]]

        aspect = (extent[1] - extent[0]) / (extent[3] - extent[2])

        output_min = min(y_data.min(), y_pred_mean.min())
        output_max = max(y_data.max(), y_pred_mean.max())
        latent_min = min(f_data.min(), f_pred_mean.min())
        latent_max = max(f_data.max(), f_pred_mean.max())

        self.imshow(axes[0], y_pred_mean, label='Output prediction', extent=extent, vmin = output_min, vmax = output_max)

        extent_data = [t_data[0, 0], t_data[-1, 0], t_data[0, 1], t_data[-1, 1]]
        if y_data is not None:
            self.imshow(axes[1], y_data, label='Output data', extent=extent_data, vmin = output_min, vmax = output_max)

        # print(torch.square(y_pred_mean - f_pred_mean).mean())
        self.imshow(axes[2], f_pred_mean, label='Latent force prediction', extent=extent, vmin = latent_min, vmax = latent_max)
        if f_data is not None:
            self.imshow(axes[3], f_data, label='Latent force data', vmin = latent_min, vmax = latent_max)
        plt.tight_layout()

    def plot_result(self, axes, t_pred, y_pred, f_pred, t_data, y_data=None, f_data=None, t_cond=None, y_cond=None, t_f_cond=None, f_cond=None, ylabels=['Predator', 'Prey']):
        y_pred_mean, y_pred_var = y_pred
        lines_out = axes[0].plot(t_pred, y_pred_mean, alpha=0.8, linewidth=0.8)[0]
        legend = [(lines_out, 'prediction')]
        [axes[0].fill_between(
            t_pred,
            y_pred_mean[:, i] - y_pred_var[:, i],
            y_pred_mean[:, i] + y_pred_var[:, i], alpha=0.1
        ) for i in range(self.n_functions)]
        axes[0].set_title('Outputs')

        if y_data is not None:
            lines_data = axes[0].plot(
                t_data[:20],
                y_data[:20],
                alpha=0.4, c='black', label='training data'
            )
            legend.append((lines_data[0], 'training data'))

        if y_cond is not None:
            scatter = [axes[0].scatter(t_cond[:20], y_cond[i][:20].t(), marker='x', s=20, alpha=0.8, label='observations')
             for i in range(y_cond.shape[0])][0]
            legend.append((scatter, 'observations'))
        axes[0].legend([a for a, _ in legend], [b for _, b in legend])

        # ax = axes[0, 3].twinx()
        f_pred_mean, f_pred_var = f_pred
        f_pred_mean = f_pred_mean.squeeze()
        axes[1].plot(t_pred, f_pred_mean, label='prediction', c='red', alpha=0.8, linewidth=.8)
        if f_data is not None:
            axes[1].plot(
                t_data[:20],
                f_data[:20],
                label='truth', c='black', alpha=0.5
            )
        axes[1].set_xlabel('Time')
        axes[1].set_ylabel(ylabels[0])
        axes[0].set_xlabel('Time')
        axes[0].set_ylabel(ylabels[1])
        if f_cond is not None:
            if t_f_cond is None:
                t_f_cond = t_cond
            axes[1].scatter(
                t_f_cond[:20],
                f_cond[:20],
                marker='x', s=20, label='ground truth')
        axes[1].fill_between(
            t_pred,
            f_pred_mean - f_pred_var/2,
            f_pred_mean + f_pred_var/2,
            alpha=0.2
        )
        
        axes[0].set_ylim((y_pred_mean[:, 0] - y_pred_var[:, 0]).min(), (y_pred_mean[:, 0] + y_pred_var[:, 0]).max())
        # axes[0].fill_between([0, .65], (y_pred_mean[:, 0] - y_pred_var[:, 0]).min(),
        #                      (y_pred_mean[:, 0] + y_pred_var[:, 0]).max(), alpha=0.1, color='grey')
        axes[1].set_title('Latent force')
        # axes[3].scatter(t_cond, self.mean_f_train[task_index], marker='x')
        axes[1].legend()
        if y_data is not None and y_data.shape[1] == 2:
            axes[2].scatter(y_data[:, 0], y_data[:, 1], s=5, marker='x', alpha=0.5)
            print(y_pred_mean.shape)
            axes[2].plot(y_pred_mean[:, 0], y_pred_mean[:, 1], c='red')
            axes[2].set_title('Phase space')
        plt.tight_layout()
