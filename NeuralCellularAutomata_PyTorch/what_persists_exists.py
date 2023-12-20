# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_WhatPersists,Exists.ipynb.

# %% auto 0
__all__ = ['SamplePool', 'mse', 'vis_batch']

# %% ../nbs/02_WhatPersists,Exists.ipynb 3
from .core import *
from .learning_to_grow import *

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import matplotlib.pyplot as plt
from tqdm import tqdm
from functools import partial

# %% ../nbs/02_WhatPersists,Exists.ipynb 8
class SamplePool:

    def __init__(self, pool_size=1024, loss_fn=None, device=def_device):
        assert loss_fn is not None, "You need to provide a loss function"
        self.pool_size = pool_size
        self.loss_fn = loss_fn
        self.reset()
    
    def make_seed(self, sz=[1, 16, TARGET_SIZE, TARGET_SIZE]):
        seed = torch.zeros(sz).to(def_device) 
        seed[:, 3:, TARGET_SIZE//2, TARGET_SIZE//2] = 1.0
        return seed

    def reset(self):
        self.seed = self.make_seed()
        self.pool = self.seed.repeat(self.pool_size, 1, 1, 1)

    def sample(self, num_samples=8):

        # selecting a random sample from the pool
        self.idxs = torch.randperm(self.pool_size)[:num_samples]
        batch = self.pool[self.idxs, ...]

        
        # find the sample in the batch with the highest loss
        losses = self.loss_fn(batch[:, :4, :, :])
        # and replace it with the seed
        # to avoid "catastrofic forgetting" 
        # (i.e. forgetting how to generate the target from the seed)
        replace_idx = torch.argmax(losses).item()
        batch[replace_idx] = self.seed[0]


        return batch
    
    def update(self, new_samples):
        new_samples = new_samples.detach()
        # replace the old samples with the newly generated ones
        self.pool[self.idxs] = new_samples

# %% ../nbs/02_WhatPersists,Exists.ipynb 10
def mse(pred, target, dim=1): 
    return ((pred - target) * (pred - target)).sum(dim).sum(dim=(1, 2))

# %% ../nbs/02_WhatPersists,Exists.ipynb 14
def vis_batch(batch):
    B, C, H, W = batch.shape
    if C > 4:
        batch = batch[:, :4, :, :]

    plt.figure(figsize=(16, 16))
    for i in range(B):
        plt.subplot(1, B, i + 1)
        plt.imshow(batch[i].detach().cpu().permute(1, 2, 0))
        plt.axis('off')    

    plt.show()