import control as ctrl
import numpy as np
import matplotlib.pyplot as plt

# Define your transfer function H here, for example:
numerator = [1]
denominator = [1, 3, 2]
H = ctrl.TransferFunction(numerator, denominator)

# Generate the frequency range (in rad/s)
omega = np.logspace(-1, 2, 500)

# Compute Bode plot data
# By setting plot=False, we tell the function to return the data instead of plotting it
mag, phase, omega = ctrl.bode(H, omega, dB=True, plot=False)

# Now we manually plot the magnitude
plt.figure()
plt.semilogx(omega, 20 * np.log10(mag))
plt.title('Bode Plot - Magnitude')
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Magnitude [dB]')

# Now we manually plot the phase
plt.figure()
plt.semilogx(omega, phase * 180 / np.pi)
plt.title('Bode Plot - Phase')
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Phase [degrees]')

plt.show()
