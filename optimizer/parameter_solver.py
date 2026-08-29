from __future__ import annotations

from numbers import Real

import numpy as np

from optimizer.regime_constraints import VALID_REGIMES, regime_contraintes


MASS_VALUES = np.arange(100.0, 501.0, 100.0)
STIFFNESS_VALUES = np.arange(10_000.0, 80_001.0, 1_000.0)
DAMPING_VALUES = np.arange(500.0, 10_001.0, 200.0)


def _validate_response(response):
    parameters = response.get("parameters")
    if not isinstance(parameters, (list, tuple)) or len(parameters) != 3:
        raise ValueError("parameters must contain exactly [mass, stiffness, damping].")
    if response.get("regime_wanted") not in VALID_REGIMES:
        raise ValueError("regime_wanted must be one of: sous, critique, sur.")
    for value in parameters:
        if value is not None and (not isinstance(value, Real) or isinstance(value, bool) or value <= 0):
            raise ValueError("Known parameters must be positive numbers or null.")


def parameter_solver(response):
    """Find valid suspension parameter combinations for the requested regime."""
    _validate_response(response)
    parameters = response["parameters"]
    defaults = [MASS_VALUES, STIFFNESS_VALUES, DAMPING_VALUES]
    candidates = [
        defaults[index] if value is None else [float(value)]
        for index, value in enumerate(parameters)
    ]
    # Parameter order is mass, stiffness, damping.
    return regime_contraintes(*candidates, response["regime_wanted"])


def parameter_solver_one(response):
    return parameter_solver(response)


def parameter_solver_two(response):
    return parameter_solver(response)


def parameter_solver_three(response):
    return parameter_solver(response)
