#Example: Bode Plot for a Transfer Function
import numpy as np
import control as ctrl
import matplotlib.pyplot as plt

# Define the transfer function H(s) = 1 / (s^2 + 2s + 1)
num = [1]
den = [1, 2, 1]
f=50
H = ctrl.TransferFunction(num, den)
omega = 2 * np.pi * f

# Plot the Bode plot
mag, phase, omega = ctrl.bode(H, dB=True,plot=False)

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



'''
Traceback (most recent call last):
  File "/home/dora/Electrical_ENGINEERING/Frequency Domain Analysis with Bode Plot.py", line 12, in <module>
    mag, phase, omega = ctrl.bode(H, dB=True)
    ^^^^^^^^^^^^^^^^^
ValueError: not enough values to unpack (expected 3, got 2)
[Finished in 1.6s with exit code 1]
[cmd: ['python3', '-u', '/home/dora/Electrical_ENGINEERING/Frequency Domain Analysis with Bode Plot.py']]
[dir: /home/dora/Electrical_ENGINEERING]
[path: /usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/var/lib/snapd/snap/bin]
'''