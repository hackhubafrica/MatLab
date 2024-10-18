import control as ctrl
import matplotlib.pyplot as plt
import numpy as np
num = [1]
den = [1, 2, 1]

H = ctrl.TransferFunction(num, den)
mag, phase, omega = ctrl.bode(H, dB=True ,plot=False)

plt.figure()
plt.subplot(2, 1, 1)
plt.semilogx(omega, 20 * np.log10(mag))
plt.title('Bode Plot')
plt.ylabel('Magnitude (dB)')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.semilogx(omega, phase * 180 / np.pi)
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Phase (degrees)')
plt.grid(True)
plt.show()

