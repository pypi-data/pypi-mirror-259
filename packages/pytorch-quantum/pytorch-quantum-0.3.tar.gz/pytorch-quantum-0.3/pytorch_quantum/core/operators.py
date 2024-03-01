"""
This module contains functions for generating tensor representations of a variety of quantum operators.
"""

__all__ = [
    "destroy",
    "create",
    "num",
    "sigmap",
    "sigmam",
    "sigmax",
    "sigmay",
    "sigmaz",
    "CNOT",
    "CNOT_reverse",
]

import torch
from .constants import SIGMA_MINUS, SIGMA_PLUS, SIGMA_X, SIGMA_Y, SIGMA_Z


def destroy(N: int, dtype=torch.complex128) -> torch.Tensor:
    """Annihilation (Lowering) Operator of Hilbert Dimension N

    Parameters
    ----------
    N : int
        Hilbert Dimension
    dtype : optional
        torch datatypes, by default torch.complex128

    Returns
    -------
    torch.Tensor
        Annihilation Operator

    Raises
    ------
    TypeError
        When Hilbert dimension is not an integer
    """
    if not isinstance(N, int):
        raise TypeError("Hilbert space dimension must be integer value")
    data = torch.sqrt(torch.arange(1, N, dtype=torch.float64))
    return torch.diag(data, 1).type(dtype)


def create(N: int, dtype=torch.complex128) -> torch.Tensor:
    """Creation (Raising) Operator of Hilbert Dimension N

    Parameters
    ----------
    N : int
        Hilbert Dimension
    dtype : optional
        torch datatype, by default torch.complex128

    Returns
    -------
    torch.Tensor
        Creation Operator

    Raises
    ------
    TypeError
        When Hilbert dimension is not an integer
    """
    if not isinstance(N, int):
        raise TypeError("Hilbert space dimension must be integer value")
    data = torch.sqrt(torch.arange(1, N, dtype=torch.float64))
    return torch.diag(data, -1).type(dtype)


def num(N: int, dtype=torch.complex128) -> torch.Tensor:
    """Number Operator of Hilbert Dimension N

    Parameters
    ----------
    N : int
        Hilbert Dimension
    dtype : optional
        torch datatype, by default torch.complex128

    Returns
    -------
    torch.Tensor
        Number Operator

    Raises
    ------
    TypeError
        When Hilbert dimension is not an integer
    """
    if not isinstance(N, int):
        raise TypeError("Hilbert space dimension must be integer value")
    data = torch.arange(0, N, dtype=torch.float64)
    return torch.diag(data).type(dtype)


def sigmap() -> torch.Tensor:
    """Return Pauli Sigma Plus Operator as torch.Tensor

    Returns
    -------
    torch.Tensor
        Pauli Sigma Plus Operator
    """
    return SIGMA_PLUS


def sigmam() -> torch.Tensor:
    """Return Pauli Sigma Minus Operator as torch.Tensor

    Returns
    -------
    torch.Tensor
        Pauli Sigma Minus Operator
    """
    return SIGMA_MINUS


def sigmax() -> torch.Tensor:
    """Return Pauli Sigma X Operator as torch.Tensor

    Returns
    -------
    torch.Tensor
        Pauli Sigma X Operator"""
    return SIGMA_X


def sigmay() -> torch.Tensor:
    """Return Pauli Sigma Y Operator as torch.Tensor

    Returns
    -------
    torch.Tensor
        Pauli Sigma Y Operator"""
    return SIGMA_Y


def sigmaz() -> torch.Tensor:
    """Return Pauli Sigma Z Operator as torch.Tensor

    Returns
    -------
    torch.Tensor
        Pauli Sigma Z Operator
    """
    return SIGMA_Z


def CNOT() -> torch.Tensor:
    """Return CNOT Operator as torch.Tensor

    Returns
    -------
    torch.Tensor
        CNOT Operator
    """
    return torch.tensor(
        [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], dtype=torch.complex128
    )


def CNOT_reverse() -> torch.Tensor:
    """Return CNOT Operator as torch.Tensor

    Notes
    -------
    This is the reverse CNOT operator where the control and
    target qubits are swapped

    Returns
    -------
    torch.Tensor
        CNOT Operator
    """
    return torch.tensor(
        [[0, 1, 0, 0], [1, 0, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]], dtype=torch.complex128
    )
