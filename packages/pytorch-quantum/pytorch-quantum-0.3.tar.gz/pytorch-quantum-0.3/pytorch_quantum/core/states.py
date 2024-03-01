"""
This module contains functions for generating tensor representations of a variety of quantum states.
"""

__all__ = ["basis"]

import torch


def basis(dim: int, n: int = 0, dtype=torch.complex128) -> torch.Tensor:
    """Return a Fock basis state vector

    Parameters
    ----------
    dim : int
        Hilbert dimension of the system
    n : int, optional
        number state, by default 0
    dtype : optional
        torch data type, by default torch.complex128

    Returns
    -------
    torch.Tensor
        Fock basis state vector

    Raises
    ------
    TypeError
        When dimension or number are not integer
    """
    if (not isinstance(dim, int)) or (not isinstance(n, int)):
        raise TypeError("dim and n must be integer")
    ket = torch.zeros(size=(dim, 1), dtype=dtype)
    ket[n, 0] = 1.0
    return ket
