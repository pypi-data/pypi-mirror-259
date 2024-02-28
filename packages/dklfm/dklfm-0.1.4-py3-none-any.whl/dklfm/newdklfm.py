from typing import Any

import numpy as np
import torch
import gpytorch
from alfi.models.mlp import MLP
from gpytorch.distributions import MultivariateNormal
import pytorch_lightning as pl
from gpytorch.constraints import LessThan
from pytorch_lightning.utilities.types import STEP_OUTPUT

from dklfm.warmup_lr_scheduler import CosineWarmupScheduler

from torch.nn import Linear


class SkipMLP(MLP):
    def __init__(self, input_dim, output_dim, latent_dim=32, num_hidden_layers=1, skip=True):
        super().__init__(input_dim, output_dim, latent_dim, num_hidden_layers)
        self.skip = skip

    def forward(self, x, use_output_head=True):
        for i, layer in enumerate(self.network.children()):
            out = layer(x)
            if i > 0 and self.skip and isinstance(layer, Linear) and out.shape[-1] == x.shape[-1]:
                x = x + out
            else:
                x = layer(x)
        return x + self.output_head(x)


class DKLFM(pl.LightningModule):
    def __init__(self, cfg, embedder, deepkernels, add_inputs=False, kernel_in_dim=32):
        super().__init__()
        self.cfg = cfg
        self.embedder = embedder
        self.kernel = self.cfg['model']['kernel']
        self.add_inputs = type(add_inputs) == int
        if self.add_inputs:
            kernel_in_dim += add_inputs
        self.nn_common, self.nn_latent, self.nn_output = deepkernels
        self.mean_module = gpytorch.means.ConstantMean().type(torch.float64)
        self.mean_module_f = gpytorch.means.ConstantMean().type(torch.float64)

        if self.kernel == 'rbf':
            self.covar_module = gpytorch.kernels.ScaleKernel(
                gpytorch.kernels.RBFKernel(ard_num_dims=kernel_in_dim, lengthscale_constraint=LessThan(1.0))
            ).type(torch.float64)
        elif self.kernel == 'periodic':
            self.covar_module = gpytorch.kernels.ScaleKernel(
                gpytorch.kernels.PeriodicKernel(ard_num_dims=kernel_in_dim)
            ).type(torch.float64)
        else:
            raise ValueError(f"Unknown kernel {self.kernel}")
        self.covar_module.base_kernel.lengthscale *= 0.5
        print(self.covar_module.base_kernel.lengthscale)
        self.noise = torch.nn.Parameter(torch.tensor(0.05, dtype=torch.float64), requires_grad=True)
        self.prior_weight = float(cfg['training']['prior_weight']) if 'prior_weight' in cfg['training'] else 1.0

        if self.cfg['training']['alternate_likelihood']:
            self.automatic_optimization = False

    def embed(self, x_cond_blocks, x_cond, y_cond):
        _batch_size = y_cond.shape[0]
        num_timepoints = x_cond.shape[1]
        num_functions = x_cond_blocks.shape[1] // num_timepoints

        y_reshaped = y_cond.reshape(_batch_size, num_functions, num_timepoints)
        y_reshaped = y_reshaped.reshape(_batch_size * num_functions, -1, 1)
        if True:
            y_reshaped = y_reshaped.type(torch.float32)
        y_emb = self.embedder(y_reshaped).mean(dim=1).type(torch.float64)  # mean over num_timepoints
        y_emb = y_emb.reshape(_batch_size, num_functions, -1)
        return y_emb

    def ystar_given_y(self, batch, x_pred):
        x_cond_blocks, x_cond, y_cond, f_cond = batch
        device = x_cond_blocks.device
        num_timepoints = x_cond.shape[1]
        num_pred_timepoints = x_pred.shape[1]
        num_functions = y_cond.shape[-1] // num_timepoints
        x_pred_blocks = x_pred.repeat(1, num_functions, 1)
        mu_y = self.mean_module(x_cond_blocks).unsqueeze(-1)
        mu_ystar = self.mean_module(x_pred_blocks).unsqueeze(-1)

        y_emb_blocks = self.embed(x_cond_blocks, x_cond, y_cond)

        z_output = self.nn_output(torch.cat([
            x_cond_blocks,
            y_emb_blocks.repeat_interleave(num_timepoints, dim=1)
        ], dim=-1))
        z_output = self.nn_common(z_output)
        z_predic = self.nn_output(torch.cat([x_pred_blocks, y_emb_blocks.repeat_interleave(num_pred_timepoints, dim=1)], dim=-1))
        z_predic = self.nn_common(z_predic)
        jitter = torch.eye(x_cond_blocks.shape[1]).to(device) * 1e-7
        if self.add_inputs:
            z_output = torch.cat([z_output, x_cond_blocks], dim=-1)
            z_predic = torch.cat([z_predic, x_pred_blocks], dim=-1)
        k_yy = self.covar_module(z_output, z_output).evaluate() + jitter
        k_ystar_y = self.covar_module(z_predic, z_output).evaluate()
        k_ystar_ystar = self.covar_module(z_predic, z_predic).evaluate()
        mu_ystar = mu_ystar + k_ystar_y @ torch.inverse(k_yy) @ (y_cond.unsqueeze(-1) - mu_y)
        jitter = torch.eye(k_ystar_ystar.shape[1]).to(device) * 1e-7
        k_ystar = k_ystar_ystar - k_ystar_y @ torch.inverse(k_yy) @ k_ystar_y.permute(0, 2, 1) + jitter
        return mu_ystar, k_ystar

    def y_given_f(self, batch):
        x_cond_blocks, x_cond, y_cond, f_cond = batch
        device = x_cond_blocks.device
        num_timepoints = x_cond.shape[1]#y_cond.shape[-1]

        mu_y = self.mean_module(x_cond_blocks).unsqueeze(-1)
        mu_f = self.mean_module_f(x_cond).unsqueeze(-1)
        jitter = torch.eye(x_cond_blocks.shape[1]).to(device) * 1e-8

        y_emb_blocks = self.embed(x_cond_blocks, x_cond, y_cond)

        y_emb = y_emb_blocks.mean(dim=1)
        y_emb = y_emb.unsqueeze(dim=1).repeat(1, num_timepoints, 1)
        z_latent = self.nn_latent(torch.cat([x_cond, y_emb], dim=-1))
        z_latent = self.nn_common(z_latent)
        # zeros = torch.zeros(y_emb.shape[0], x_cond_blocks.shape[1], y_emb.shape[2]).to(device)

        z_output = self.nn_output(torch.cat([
            x_cond_blocks,
            y_emb_blocks.repeat_interleave(num_timepoints, dim=1)
        ], dim=-1))
        z_output = self.nn_common(z_output)
        if self.add_inputs:
            z_output = torch.cat([z_output, x_cond_blocks], dim=-1)
            z_latent = torch.cat([z_latent, x_cond], dim=-1)
        k_yf = self.covar_module(z_output, z_latent).evaluate()
        k_yy = self.covar_module(z_output, z_output).evaluate()
        k_ff = self.covar_module(z_latent, z_latent).evaluate() + jitter
        inv_k_ff = torch.inverse(k_ff)
        jitter = torch.eye(k_yy.shape[1]).to(device) * 1e-7

        mu_y_f = mu_y + k_yf @ inv_k_ff @ (f_cond.unsqueeze(-1) - mu_f)
        noise = torch.eye(k_yy.shape[1]).to(device) * self.noise
        k_y_f = k_yy - k_yf @ inv_k_ff @ k_yf.permute(0, 2, 1) + jitter + noise
        return mu_y_f, k_y_f, mu_f, k_ff

    def f_given_y(self, batch, x_pred=None):
        x_cond_blocks, x_cond, y_cond, f_cond = batch
        if x_pred is None:
            x_pred = x_cond
        # We seek mu_f|y, k_f|y, mu_y, k_yy
        # mu:
        device = x_cond_blocks.device
        mu_y = self.mean_module(x_cond_blocks).unsqueeze(-1)
        mu_f = self.mean_module_f(x_pred).unsqueeze(-1)

        num_timepoints = x_cond.shape[1]#y_cond.shape[-1]
        num_timepoints_pred = x_pred.shape[1]#y_cond.shape[-1]

        y_emb_blocks = self.embed(x_cond_blocks, x_cond, y_cond)
        y_emb = y_emb_blocks.mean(dim=1)  # mean over functions
        y_emb = y_emb.unsqueeze(dim=1).repeat(1, num_timepoints_pred, 1)
        # print(f"y {y_cond.shape} --> y_reshaped {y_reshaped.shape} --> y_emb {y_emb.shape}")
        z_latent = self.nn_latent(torch.cat([x_pred, y_emb], dim=-1))
        z_latent = self.nn_common(z_latent)

        z_output = self.nn_output(torch.cat([x_cond_blocks, y_emb_blocks.repeat_interleave(num_timepoints, dim=1)], dim=-1))
        z_output = self.nn_common(z_output)
        if self.add_inputs:
            z_output = torch.cat([z_output, x_cond_blocks], dim=-1)
            z_latent = torch.cat([z_latent, x_pred], dim=-1)

        # plt.imshow(k_yy[0].detach())
        # plt.colorbar()
        k_yy = self.covar_module(z_output, z_output).add_jitter(1e-5)
        k_ff = self.covar_module(z_latent, z_latent).evaluate()
        k_fy = self.covar_module(z_latent, z_output).evaluate()
        # plt.figure()
        # plt.imshow(k_ff.detach()[0].cpu())
        # plt.colorbar()
        # inv_k_yy = torch.inverse(k_yy)
        mu_f_y = mu_f + k_fy.matmul(k_yy.inv_matmul(y_cond.unsqueeze(-1) - mu_y))
        jitter = torch.eye(k_ff.shape[1]).to(device) * 1e-7
        noise = torch.eye(k_ff.shape[1]).to(device) * self.noise
        k_f_y = k_ff - k_fy @ (k_yy.inv_matmul(k_fy.transpose(-1, -2))) + noise
        return mu_f_y, k_f_y, mu_y, k_yy

    def on_train_batch_end(self, outputs: STEP_OUTPUT, batch: Any, batch_idx: int) -> None:
        self.log("noise", self.noise.item())
        self.log("lengthscale", self.covar_module.base_kernel.lengthscale.mean().item())
        self.noise.data.clamp_(0., .1)
        if self.kernel == 'periodic':
            self.log('kernel_period', self.model.covar_module.base_kernel.period_length.mean().item())

        super().on_train_batch_end(outputs, batch, batch_idx)

    def generic_step(self, batch):
        x_cond_blocks, x_cond, y_cond, f_cond = batch
        if False:
            mu_y_f, k_y_f, mu_f, k_ff = self.y_given_f(batch)
            loss_cond = -MultivariateNormal(mu_y_f.squeeze(), k_y_f).log_prob(y_cond).mean()
            loss_prior = -MultivariateNormal(mu_f.squeeze(), k_ff).log_prob(f_cond).mean()
            mse = torch.square(mu_y_f.squeeze() - y_cond).mean()
        else:
            mu_f_y, k_f_y, mu_y, k_yy = self.f_given_y(batch)
            loss_cond = -MultivariateNormal(mu_f_y.squeeze(), k_f_y).log_prob(f_cond).mean()
            loss_prior = -MultivariateNormal(mu_y.squeeze(), k_yy).log_prob(y_cond).mean()
            mse = torch.square(mu_f_y.squeeze() - f_cond).mean()

        self.log("mse", mse.item())
        self.log("noise", self.noise.item())
        return loss_cond + self.prior_weight * loss_prior + 1000 * mse, loss_prior, loss_cond

    def training_step(self, batch, batch_idx):
        loss_batch, loss_prior, loss_cond = self.generic_step(batch)
        self.log("train_loss", loss_batch)
        self.log('train_loss_prior', loss_prior.item())
        self.log('train_loss_cond', loss_cond.item())

        if self.cfg['training']['gradient_clip_val']:
            torch.nn.utils.clip_grad_norm_(self.parameters(), self.cfg['training']['gradient_clip_val'])

        if (self.current_epoch % 5) == 0:
            self.harmonic_mse_step(batch)
        return loss_batch

    def harmonic_mse_step(self, batch):
        with torch.no_grad():
            x_cond_blocks, x_cond, y_cond, f_cond = batch
            mu_f_y, k_f_y, _, _ = self.f_given_y(batch)
            mu_f_y = mu_f_y
            mu_y, k_y = self.ystar_given_y(batch, batch[1])
            mse_latent = torch.square(f_cond - mu_f_y.squeeze()).mean()
            mse_output = torch.square(y_cond - mu_y.squeeze()).mean()
            harmonic_mse = 2 * mse_latent * mse_output / (mse_latent + mse_output)

        self.log("harmonic_mse", harmonic_mse.item())

    def validation_step(self, batch, batch_idx):
        with torch.no_grad():
            loss_batch, loss_prior, loss_cond = self.generic_step(batch)
        self.log('val_loss', loss_batch.item())
        self.log('val_loss_prior', loss_prior.item())
        self.log('val_loss_cond', loss_cond.item())

    def configure_optimizers(self):
        lr = float(self.cfg['training']['lr'])
        alternate_likelihood = self.cfg['training']['alternate_likelihood']
        params = [{'params': self.parameters()}]
        if self.cfg['training']['optimizer_type'] == 'LBFGS':
            optimizer_y = torch.optim.LBFGS(params)
            optimizer_f = torch.optim.LBFGS(params)
        else:
            optimizer_y = torch.optim.Adam(params, lr=lr, weight_decay=self.cfg['training']['weight_decay'])
            optimizer_f = torch.optim.Adam(params, lr=lr, weight_decay=self.cfg['training']['weight_decay'])
        optimizers = optimizer_y
        if alternate_likelihood:
            optimizers = [optimizer_y, optimizer_f]

        if self.cfg['training']['add_schedulers']:
            lr_scheduler_y = CosineWarmupScheduler(
                optimizer_y, warmup=self.cfg['training']['warmup'], max_iters=self.cfg['training']['warmup_max_iters']
            )
            lr_scheduler_f = CosineWarmupScheduler(
                optimizer_f, warmup=self.cfg['training']['warmup'], max_iters=self.cfg['training']['warmup_max_iters']
            )
            schedulers = [
                {'scheduler': lr_scheduler_y, 'interval': 'step'},
                {'scheduler': lr_scheduler_f, 'interval': 'step'}
            ]
            return optimizers, schedulers

        return optimizers
