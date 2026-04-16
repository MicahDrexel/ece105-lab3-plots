"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np
import matplotlib.pyplot as plt


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

def main():
    sensor_a, sensor_b, timestamps = generate_data(seed=9811)
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    plot_scatter(sensor_a, sensor_b, timestamps, axes[0, 0])

    axes[0, 1].hist(sensor_a, bins=30, alpha=0.5, color='tab:blue', label='Sensor A')
    axes[0, 1].hist(sensor_b, bins=30, alpha=0.5, color='tab:orange', label='Sensor B')
    axes[0, 1].axvline(sensor_a.mean(), color='tab:blue', linestyle='--', linewidth=1.5, label='Sensor A mean')
    axes[0, 1].axvline(sensor_b.mean(), color='tab:orange', linestyle='--', linewidth=1.5, label='Sensor B mean')
    axes[0, 1].set_xlabel('Temperature (°C)')
    axes[0, 1].set_ylabel('Count')
    axes[0, 1].set_title('Overlaid temperature distributions')
    axes[0, 1].legend()
    axes[0, 1].grid(True)

    axes[1, 0].boxplot([sensor_a, sensor_b], labels=['Sensor A', 'Sensor B'], patch_artist=True,
                       boxprops=dict(facecolor='lightgray', color='black'),
                       medianprops=dict(color='red'))
    axes[1, 0].set_title('Sensor temperature box plots')
    axes[1, 0].set_ylabel('Temperature (°C)')
    axes[1, 0].grid(True, axis='y')

    axes[1, 1].axis('off')
    summary_text = (
        f"Sensor A mean: {sensor_a.mean():.2f} °C\n"
        f"Sensor A std: {sensor_a.std(ddof=1):.2f} °C\n\n"
        f"Sensor B mean: {sensor_b.mean():.2f} °C\n"
        f"Sensor B std: {sensor_b.std(ddof=1):.2f} °C"
    )
    axes[1, 1].text(0.02, 0.98, 'Summary statistics', transform=axes[1, 1].transAxes,
                    fontsize=12, fontweight='bold', va='top')
    axes[1, 1].text(0.02, 0.78, summary_text, transform=axes[1, 1].transAxes,
                    fontsize=10, va='top')

    fig.tight_layout()
    fig.savefig('sensor_plots_grid.png', dpi=300)
    plt.close(fig)


if __name__ == '__main__':
    main()
