"""
This module contains common constants for quantum physics modelling.
"""

__all__ = ["SIGMA_X", "SIGMA_Y", "SIGMA_Z", "SIGMA_PLUS", "SIGMA_MINUS"]

import torch

SIGMA_X = torch.tensor([[0, 1], [1, 0]], dtype=torch.complex128)
SIGMA_Y = torch.tensor([[0, -1j], [1j, 0]], dtype=torch.complex128)
SIGMA_Z = torch.tensor([[1, 0], [0, -1]], dtype=torch.complex128)
SIGMA_PLUS = torch.tensor([[0, 1], [0, 0]], dtype=torch.complex128)
SIGMA_MINUS = torch.tensor([[0, 0], [1, 0]], dtype=torch.complex128)
