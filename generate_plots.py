"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np


def generate_data(seed):
    """Generate synthetic sensor temperature data.

    Parameters
    ----------
    seed : int
        Seed for NumPy's random number generator to ensure reproducible
        synthetic sensor readings.

    Returns
    -------
    sensor_a : numpy.ndarray
        Array of shape (200,) containing Sensor A temperature readings in
        degrees Celsius with mean 25 and standard deviation 3.
    sensor_b : numpy.ndarray
        Array of shape (200,) containing Sensor B temperature readings in
        degrees Celsius with mean 27 and standard deviation 4.5.
    timestamps : numpy.ndarray
        Array of shape (200,) containing timestamps uniformly spaced from
        0 to 10 seconds.
    """
    rng = np.random.default_rng(seed)
    num_readings = 200
    timestamps = np.linspace(0, 10, num_readings, dtype=np.float64)
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=num_readings).astype(np.float64)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=num_readings).astype(np.float64)
    return sensor_a, sensor_b, timestamps