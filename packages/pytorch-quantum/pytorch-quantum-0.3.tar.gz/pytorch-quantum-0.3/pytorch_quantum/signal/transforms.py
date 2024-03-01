"""
This module contains tools for typical signal transforms used for modelling
and processing the drive in quantum dynamics
"""

__all__ = ["pad_zeros", "lowpass_filter"]

import torch
import torch.nn.functional as F
from typing import Tuple


def pad_zeros(signal: torch.Tensor, pad_pixels: Tuple[int, int]) -> torch.Tensor:
    """Pad a signal with zeros at the beginning and end

    Parameters
    ----------
    signal : torch.Tensor
        1D signal to be padded
    pad_pixels : Tuple[int, int]
        Tuple of pixels to pad at (beginning, end)

    Returns
    -------
    torch.Tensor
        Padded signal
    """
    return F.pad(signal, pad_pixels, "constant", 0)


def lowpass_filter(signal: torch.Tensor, cutoff: int) -> torch.Tensor:
    """Low pass filter a signal

    Parameters
    ----------
    signal : torch.Tensor
        Original 1D signal
    cutoff : int
        Components to keep from original signal FFT

    Returns
    -------
    torch.Tensor
        Filtered signal
    """
    # FFT of the original signal
    S = torch.fft.fft(signal)

    f_c = cutoff  # Cut-off frequency
    H = torch.zeros_like(S)
    H[:f_c] = 1
    H[-f_c:] = 1
    # Apply the filter by multiplying in frequency domain
    Y = S * H
    # Inverse FFT to get the smoothed signal
    return torch.fft.ifft(Y).real
