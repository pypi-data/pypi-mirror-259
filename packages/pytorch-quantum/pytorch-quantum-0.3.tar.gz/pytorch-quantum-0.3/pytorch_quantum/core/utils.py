"""
This module contains common utilities for quantum physics modelling.
"""

__all__ = [
    "normalise",
    "expect",
    "dagger",
    "project_unitary_comp",
    "calculate_fidelity",
]

import torch
import warnings
from .states import basis


def normalise(statevector: torch.Tensor) -> torch.Tensor:
    """Return a normalised statevector

    Parameters
    ----------
    statevector : torch.Tensor
        Input state as a ket

    Returns
    -------
    torch.Tensor
        Normalise states as a ket

    Raises
    -------
    TypeError
        If the input is not a statevector of shape n x 1

    """
    # normalise to unity
    if (len(statevector.shape) != 2) and (statevector.shape[-1] != 1):
        raise TypeError("Invalid dimensions: Provide a statevector of shape n x 1")
    return torch.nn.functional.normalize(statevector, p=2, dim=0)


def expect(operator: torch.Tensor, ket: torch.Tensor) -> torch.Tensor:
    """Return the expectation value of an operator

    Parameters
    ----------
    operator : torch.Tensor
        Operator to calculate the expectation value of
    ket : torch.Tensor
        Statevector to calculate the expectation value of

    Returns
    -------
    torch.Tensor
        Expectation value of the operator

    Raises
    -------
    TypeError
        If the input is not a statevector of shape n x 1

    """
    if (len(ket.shape) != 2) and (ket.shape[-1] != 1):
        raise TypeError("Invalid dimensions: Provide a statevector of shape n x 1")
    return torch.matmul(torch.conj(ket.T), torch.matmul(operator, ket)).real


def dagger(input: torch.Tensor) -> torch.Tensor:
    """Return the Hermitian Conjugate of the input

    Parameters
    ----------
    input : torch.Tensor
        Input tensor

    Returns
    -------
    torch.Tensor
        Hermitian Conjugate
    """
    return torch.conj(torch.transpose(input, 0, 1))


def project_unitary_comp(U: torch.Tensor) -> torch.Tensor:
    """Project a given unitary to the computational subspace

    Parameters
    ----------
    U : torch.Tensor
        Original unitary

    Returns
    -------
    torch.Tensor
        Unitary projected to the computational subspace
    """

    warnings.warn("This function is not yet implemented completely", UserWarning)

    psi0 = basis(U.shape[0], 0)
    psi1 = basis(U.shape[0], 1)

    P = (psi0 @ dagger(psi0)) + (psi1 @ dagger(psi1))
    U_projected = P @ U @ (dagger(P))
    return U_projected


def calculate_fidelity(U, V):
    """Calculate the fidelity between two unitary matrices U and V.

    Parameters
    ----------
    U : torch.Tensor
        Unitary matrix for which to calculate the fidelity
    V : torch.Tensor
        Target unitary matrix

    Returns
    -------
    float
        The fidelity between the two unitary matrices
    """
    # Ensure U and V are square matrices and have the same dimensions
    assert (
        U.size(0) == U.size(1) == V.size(0) == V.size(1)
    ), "U and V must be square matrices of the same dimension."

    # Calculate V†U
    V_dagger_U = torch.matmul(V.conj().t(), U)

    # Calculate the trace of V†U
    trace_V_dagger_U = torch.trace(V_dagger_U)

    # Normalize by the dimension N
    N = U.size(0)
    normalized_trace = trace_V_dagger_U / N

    # Calculate the fidelity
    fidelity = torch.abs(normalized_trace) ** 2

    return fidelity.item()
