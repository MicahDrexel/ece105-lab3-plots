# Sensor Plot Generation

A small script to generate synthetic temperature sensor data and save publication-style visualizations as PNG files.

## Installation

1. Activate the `ece105` conda environment:
   ```bash
   conda activate ece105
   ```
2. Install the required dependencies using conda or mamba:
   ```bash
   conda install numpy matplotlib
   ```
   or
   ```bash
   mamba install numpy matplotlib
   ```

## Usage

Run the script from the project directory:

```bash
python generate_plots.py
```

## Example output

The script produces a set of figure files showing the synthetic sensor data:

- A scatter plot of Sensor A and Sensor B temperature readings versus time.
- An overlaid histogram comparing the temperature distributions of the two sensors.
- A box plot summarizing the temperature distributions for Sensor A and Sensor B.

## AI tools used and disclosure

Placeholder paragraph for AI tools used and any relevant disclosure details.
