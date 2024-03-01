"""Contains the sesolve function for solving the Schrodinger Equation for time-dependent
and time-independent Hamiltonians"""

__all__ = ["sesolve", "sesolve_t_steps"]

import torch


def sesolve(dHs: torch.Tensor, dt: torch.Tensor) -> torch.Tensor:
    """Generate the unitary propagator for both time-dependent and time-independent Hamiltonians.
    Works by exponentiating the differential Hamiltonian elements (piecewise constant approximation)
    and then multipying all the differential time evolution operator elements.

    Parameters
    ----------
    dHs : torch.Tensor
        Differential Hamiltonian Elements
    dt : torch.Tensor
        Duration of time step used for discretisation

    Returns
    -------
    torch.Tensor
        Propagator
    """
    dUs = torch.linalg.matrix_exp(-1j * dHs * dt)
    return _compile_propagators(dUs)


def sesolve_t_steps(
    dHs: torch.Tensor, dt: torch.Tensor, t_steps: torch.Tensor
) -> list[torch.Tensor]:
    """Generate the unitary propagator for both time-dependent and time-independent Hamiltonians.
    Works by selecting the subset of differential Hamiltonian elements for t_steps and exponentiating
    (piecewise constant approximation) and then multipying all the differential time evolution
    operator elements. It stores and returns the intermediate compiled unitaries to allow the visualisation of
    complete time evolution.

    This method is not differentiable or jit-able and is only used for visualisation purposes.

    Use ::code:`sesolve()` to generate the single complete propagator and ::code:`sesolve_t_steps()` to
    generate the full time-series of propagators.

    Parameters
    ----------
    dHs : torch.Tensor
        Differential Hamiltonian Elements
    dt : torch.Tensor
        Duration of time step used for discretisation
    t_steps : torch.Tensor
        Total number of time steps to evolve

    Returns
    -------
    list[torch.Tensor]
        List of Propagators
    """
    dUs = torch.linalg.matrix_exp(-1j * dHs[:t_steps, ...] * dt)
    Us: list[torch.Tensor] = [None] * len(dUs)
    Us[0] = dUs[0]
    for i in range(1, len(dUs)):
        Us[i] = Us[i - 1] @ dUs[i]
    return Us


def _compile_propagators(dUs: torch.Tensor) -> torch.Tensor:
    """Compile the propagators into a single propagator.

    Parameters
    ----------
    dUs : torch.Tensor
        Differential propagators

    Returns
    -------
    torch.Tensor
        Compiled propagator

    """
    U = dUs[0, ...]
    for i in range(1, len(dUs)):
        U = U @ dUs[i, ...]
    return U


def _compile_propagators_recursive(dUs: torch.Tensor) -> torch.Tensor:
    """Compile the propagators into a single propagator, recursively.

    Parameters
    ----------
    dUs : torch.Tensor
        Differential propagators

    Returns
    -------
    torch.Tensor
        Compiled propagator

    """
    if dUs.shape[0] == 1:
        return dUs[0]
    elif dUs.shape[0] == 2:
        return dUs[1] @ dUs[0]
    else:
        len = dUs.shape[0]
        midpoint = len // 2
        return _compile_propagators(dUs[midpoint:, ...]) @ _compile_propagators(
            dUs[:midpoint, ...]
        )
