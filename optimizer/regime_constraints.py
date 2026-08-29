from __future__ import annotations

from itertools import product
from numbers import Real

import numpy as np


VALID_REGIMES = {"sous", "critique", "sur"}


def _values(value):
    """Return a one-dimensional iterable for either a scalar or an array-like."""
    if isinstance(value, Real) and not isinstance(value, bool):
        return [float(value)]
    array = np.asarray(value, dtype=float).reshape(-1)
    return array.tolist()


def _matches(delta: float, nature: str) -> bool:
    if nature not in VALID_REGIMES:
        raise ValueError(f"Unknown regime '{nature}'. Use sous, critique, or sur.")
    if nature == "sous":
        return delta < 1.0
    if nature == "sur":
        return delta > 1.0
    return bool(np.isclose(delta, 1.0, rtol=1e-6, atol=1e-8))


def regime_contraintes(m, k, c, nature: str):
    """Return all positive (mass, stiffness, damping) combinations in a regime."""
    if nature not in VALID_REGIMES:
        raise ValueError(f"Unknown regime '{nature}'. Use sous, critique, or sur.")

    masses, stiffnesses, dampings = _values(m), _values(k), _values(c)
    if any(value <= 0 for value in masses + stiffnesses + dampings):
        raise ValueError("Mass, stiffness, and damping values must be positive.")

    result = []
    for mass, stiffness, damping in product(masses, stiffnesses, dampings):
        delta = damping / (2.0 * np.sqrt(mass * stiffness))
        if _matches(delta, nature):
            result.append((mass, stiffness, damping))
    return result


# Backward-compatible helpers retained for callers from the original project.
def computing_one_mass(a, x, y, nature):
    return regime_contraintes(a, x, y, nature)


def computing_one_raider(a, x, y, nature):
    return regime_contraintes(x, a, y, nature)


def computing_one_friction(a, x, y, nature):
    return regime_contraintes(x, y, a, nature)


def computing_two_friction(m, k, c, nature):
    return regime_contraintes(m, k, c, nature)


def computing_two_raideur(m, k, c, nature):
    return regime_contraintes(m, k, c, nature)


def computing_two_mass(m, k, c, nature):
    return regime_contraintes(m, k, c, nature)


def computing_three(m, k, c, nature):
    return regime_contraintes(m, k, c, nature)
