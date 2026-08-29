from __future__ import annotations

from physics.equations import equation_finder


def computing_amplitude(list_data, response):
    """Compute peak absolute displacement and final simulation time per candidate."""
    amplitudes = []
    time_stops = []
    for system_parameters in list_data:
        time, displacement = equation_finder(response, system_parameters)
        amplitudes.append(float(max(abs(float(value)) for value in displacement)))
        time_stops.append(float(time[-1]) if len(time) else 0.0)
    return amplitudes, time_stops
