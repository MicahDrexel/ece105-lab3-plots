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

# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Draw a sensor temperature scatter plot on an existing Axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Array of shape (200,) containing Sensor A temperature readings in
        degrees Celsius.
    sensor_b : numpy.ndarray
        Array of shape (200,) containing Sensor B temperature readings in
        degrees Celsius.
    timestamps : numpy.ndarray
        Array of shape (200,) containing timestamps in seconds.
    ax : matplotlib.axes.Axes
        Axes object to draw the scatter plot on.

    Returns
    -------
    None
        The function modifies the provided Axes object in place.
    """
    ax.scatter(timestamps, sensor_a, color='tab:blue', label='Sensor A', alpha=0.7)
    ax.scatter(timestamps, sensor_b, color='tab:orange', label='Sensor B', alpha=0.7)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Sensor Temperature Readings vs Time')
    ax.legend()
    ax.grid(True)
    return None