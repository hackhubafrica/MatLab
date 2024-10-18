import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Define the transfer function H(s)
numerator = [1]
denominator = [1, 1]
H = ctrl.TransferFunction(numerator, denominator)

# Frequency range for Bode plot
omega = np.logspace(-1, 2, 1000)

# Calculate magnitude and phase
mag, phase, omega = ctrl.bode(H, omega,plot=False)

# Plot the Bode plot
plt.figure()
plt.subplot(2, 1, 1)
plt.semilogx(omega, 20 * np.log10(mag))
plt.title('Bode Plot: Magnitude Response')
plt.ylabel('Magnitude (dB)')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.semilogx(omega, phase * 180 / np.pi)
plt.title('Bode Plot: Phase Response')
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Phase (degrees)')
plt.grid(True)

plt.tight_layout()
plt.show()