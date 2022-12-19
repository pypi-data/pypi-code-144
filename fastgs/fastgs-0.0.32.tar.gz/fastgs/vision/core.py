# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/07a_vision.core.ipynb.

# %% ../../nbs/07a_vision.core.ipynb 1
from __future__ import annotations

# %% auto 0
__all__ = ['TensorImageMS']

# %% ../../nbs/07a_vision.core.ipynb 3
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from IPython.display import display, HTML

from fastai.vision.all import *

# %% ../../nbs/07a_vision.core.ipynb 5
class TensorImageMS(TensorImage):
    "Class to represent multi-spectral data (more than 3 channels)"
    pass

# %% ../../nbs/07a_vision.core.ipynb 7
@patch(cls_method=True)
def from_tensor(
    cls:TensorImageMS,
    x, # tensor of channels
    bands:list(tuple(int)), # list of index position tuples, each tuple is 3 ordered channel indices or a single channel index
    captions:list(str), # list of captions for each set of bands
    brgtX:list(list(float)), # list of brightness multiplier lists, each list has a multiplier for each element of the corresponding channel tuple
):
    return cls(x, bands=bands, captions=captions, brgtX=brgtX)

@patch(cls_method=True)
def from_tensor_bands(
    cls:TensorImageMS,
    x, # tensor of channels
    bands:list(tuple(int)), # list of index position tuples, each tuple is 3 ordered channels or a single channel
    captions:list(str) # list of captions for each set of bands
):
    return cls.from_tensor(x, bands=bands, captions=captions, brgtX=[[1] * len(i) for i in bands])

# %% ../../nbs/07a_vision.core.ipynb 11
@patch
def num_images(self: TensorImageMS) -> int:
    return len(self.bands)

# %% ../../nbs/07a_vision.core.ipynb 14
@patch
def _select_bands(self: TensorImageMS, bands: tuple[int]) -> TensorImageMS:
    assert len(bands) == 3 or len(bands) == 1
    return torch.index_select(self, 0, torch.IntTensor(bands))

# %% ../../nbs/07a_vision.core.ipynb 17
@patch
def _brighten(self: TensorImageMS, brgtX: list[float]) -> TensorImageMS:
    assert self.shape[0] == len(brgtX)
    brdcsts = [None] * max(0, len(self.shape) - 1)
    multX = reduce(lambda mX, _: mX.unsqueeze(-1), brdcsts, Tensor(brgtX))
    return torch.clamp(self * multX, 0, 1)

# %% ../../nbs/07a_vision.core.ipynb 23
@patch
def _show_tiles(self: TensorImageMS, ctxs: list, **kwargs) -> list:
    assert ctxs is not None
    ims = [self._select_bands(b)._brighten(m) for b, m in zip(self.bands, self.brgtX)]
    return [show_image(im, ax=ax, title=t) for im, t, ax in zip(ims, self.captions, ctxs)]

# %% ../../nbs/07a_vision.core.ipynb 25
@patch
def _get_grid(self: TensorImageMS, nrows: int, **kwargs) -> list:
    ncols = self.num_images()
    ncells = nrows * ncols
    return get_grid(ncells, nrows, ncols, **kwargs)

# %% ../../nbs/07a_vision.core.ipynb 27
@patch
def show(self: TensorImageMS, ctxs=None, **kwargs) -> list:
    ctxs = self._get_grid(1, **kwargs) if ctxs is None else ctxs
    return self._show_tiles(ctxs=ctxs, **kwargs)

# %% ../../nbs/07a_vision.core.ipynb 35
@patch
def _show_animation(self: TensorImageMS):
    fig, ax = plt.subplots()
    ax.axis("off")
    ims = [
        [ax.imshow(self._select_bands(b)._brighten(m).permute(1, 2, 0), animated=True)]
        for b, m in zip(self.bands, self.brgtX)
    ]
    anim = animation.ArtistAnimation(fig, ims, interval=1000, blit=True)
    plt.close()
    display(HTML(anim.to_html5_video()))
