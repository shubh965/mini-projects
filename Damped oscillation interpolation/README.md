# Damped Oscillation Interpolation & Envelope Fitting

A lightweight Python utility to analyse damped oscillatory peak values, fit exponential decay envelopes, and reconstruct the continuous oscillating waveform.

## Features

- **Decay Envelope Fitting**: Fits upper ($A_0 e^{-bt}$) and lower ($-A_0 e^{-bt}$) decay envelopes using non-linear least squares curve fitting (`scipy.optimize.curve_fit`).
- **Waveform Reconstruction**: Reconstructs the continuous damped oscillatory waveform based on input extrema.
- **Visualization**: Generates and displays a plot with the fitted envelopes, reconstructed wave, and data points, and exports it as `damped_oscillation.png`.


## Requirements

- Python 3.8+
- NumPy
- SciPy
- Matplotlib

Install dependencies via pip:
```bash
pip install numpy scipy matplotlib
```


## Usage

1. Run the script:
   ```bash
   python damped_oscillation.py
   ```

2. When prompted, enter comma-separated peak values (consecutive crests and troughs):
   ```text
   Enter comma-separated peak values (eg: 10.0, -8.2, 6.7, -5.5): 10.0, -8.2, 6.7, -5.5, 4.5, -3.7
   ```

3. The script will output the estimated initial amplitude ($A_0$) and damping factor ($b$), display the interactive plot, and save the result to `damped_oscillation.png`.
