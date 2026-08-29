from __future__ import annotations

import numpy as np


def _system_values(system_parameters, pos, speed):
    if len(system_parameters) != 3:
        raise ValueError("system_parameters must be (mass, stiffness, damping).")
    mass, stiffness, damping = (float(value) for value in system_parameters)
    if min(mass, stiffness, damping) <= 0:
        raise ValueError("Mass, stiffness, and damping must be positive.")
    return mass, stiffness, damping, float(pos or 0.0), float(speed or 0.0)


def _time_axis(t_max):
    return np.linspace(0.0, max(float(t_max), 0.01), 1000)


def equation_sous_regime(system_parameters, pos=0.0, speed=0.0):
    mass, stiffness, damping, pos, speed = _system_values(system_parameters, pos, speed)
    delta = damping / (2.0 * np.sqrt(mass * stiffness))
    omega_n = np.sqrt(stiffness / mass)
    omega_d = omega_n * np.sqrt(max(1.0 - delta**2, np.finfo(float).eps))
    A = pos
    B = (speed + delta * omega_n * pos) / omega_d
    settling_time = 4.0 / max(delta * omega_n, np.finfo(float).eps)
    t = _time_axis(5.0 * settling_time)
    y = np.exp(-delta * omega_n * t) * (A * np.cos(omega_d * t) + B * np.sin(omega_d * t))
    return t, y


def equation_critique_regime(system_parameters, pos=0.0, speed=0.0):
    mass, stiffness, damping, pos, speed = _system_values(system_parameters, pos, speed)
    omega_n = np.sqrt(stiffness / mass)
    delta = damping / (2.0 * np.sqrt(mass * stiffness))
    B = speed + omega_n * pos
    settling_time = 4.0 / max(delta * omega_n, np.finfo(float).eps)
    t = _time_axis(5.0 * settling_time)
    y = (pos + B * t) * np.exp(-omega_n * t)
    return t, y


def equation_sur_regime(system_parameters, pos=0.0, speed=0.0):
    mass, stiffness, damping, pos, speed = _system_values(system_parameters, pos, speed)
    delta = damping / (2.0 * np.sqrt(mass * stiffness))
    omega_n = np.sqrt(stiffness / mass)
    root = np.sqrt(max(delta**2 - 1.0, np.finfo(float).eps))
    r1 = -omega_n * (delta + root)
    r2 = -omega_n * (delta - root)
    A = (speed - r2 * pos) / (r1 - r2)
    B = (r1 * pos - speed) / (r1 - r2)
    settling_time = 4.0 / max(delta * omega_n, np.finfo(float).eps)
    t = _time_axis(5.0 * settling_time)
    y = A * np.exp(r1 * t) + B * np.exp(r2 * t)
    return t, y


def equation_finder(response, system_parameters):
    regime = response.get("regime_wanted")
    pos = response.get("initial_position", 0.0)
    speed = response.get("initial_speed", 0.0)
    if regime == "sous":
        return equation_sous_regime(system_parameters, pos, speed)
    if regime == "critique":
        return equation_critique_regime(system_parameters, pos, speed)
    if regime == "sur":
        return equation_sur_regime(system_parameters, pos, speed)
    raise ValueError("regime_wanted must be one of: sous, critique, sur.")
