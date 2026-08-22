import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def exponential_decay(t, A0, b):
    return A0 * np.exp(-b * t) # A(t) = A0 * e^-bt

def main():
    input_str = input("Enter comma-separated peak values (eg: 10.0, -8.2, 6.7, -5.5): ")
    
    try:
        raw_amplitudes = np.array([float(x.strip()) for x in input_str.split(',')])
    except ValueError:
        print("Invalid input. Please ensure you enter comma-separated numbers.")
        return

    if len(raw_amplitudes) < 2:
        print("Error: At least 2 points are required for damping analysis.")
        return

    times = np.arange(len(raw_amplitudes))
    magnitudes = np.abs(raw_amplitudes)

    ln_A = np.log(magnitudes)
    slope, intercept = np.polyfit(times, ln_A, 1)
    b_init = max(-slope, 1e-6)
    A0_init = np.exp(intercept)

    try:
        popt, _ = curve_fit(
            exponential_decay,
            times,
            magnitudes,
            p0 = [A0_init, b_init],
            bounds = ([0, 0], [np.inf, np.inf]),
            maxfev = 5000
        )
        A0_opt, b_opt = popt
    except Exception:
        A0_opt, b_opt = A0_init, b_init

    print(f"\nInitial Amplitude (A0): {A0_opt:.3f}")
    print(f"Calculated Damping Factor (b): {b_opt:.3f}")


    t_smooth = np.linspace(0, times[-1], 200)
    A_upper = exponential_decay(t_smooth, A0_opt, b_opt)
    A_lower = -A_upper
    plt.figure(figsize = (9, 5.5))
    
    plt.plot(t_smooth, A_upper, 'r--', linewidth = 2, label = f'Upper Envelope: $A_0 e^{{-bt}}$')
    plt.plot(t_smooth, A_lower, 'b--', linewidth = 2, label = f'Lower Envelope: $-A_0 e^{{-bt}}$')
    
    initial_sign = np.sign(raw_amplitudes[0]) if len(raw_amplitudes) > 0 else 1
    x_wave = initial_sign * exponential_decay(t_smooth, A0_opt, b_opt) * np.cos(np.pi * t_smooth)
    
    plt.plot(t_smooth, x_wave, color = 'gray', linestyle = '-', alpha = 0.6, label = 'Reconstructed Waveform')
    plt.plot(times, raw_amplitudes, 'ko', markersize = 7, label = 'Inputted Peak Values', zorder = 5)
    
    plt.axhline(0, color = 'gray', linestyle = ':', alpha = 0.7)
    plt.title("Damped Oscillation and Decay Envelope", fontsize = 12, fontweight = "bold")
    plt.xlabel("Time (s)")
    plt.ylabel("Displacement (cm)")
    plt.legend(loc = "upper right")
    plt.grid(True, linestyle = "--", alpha = 0.6)
    
    plt.savefig("damped_oscillation.png", dpi = 150, bbox_inches = "tight")
    plt.show()

if __name__ == "__main__":
    main()
