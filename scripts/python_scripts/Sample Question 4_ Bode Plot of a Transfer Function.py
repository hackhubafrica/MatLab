'''
Sample Question 4: Bode Plot of a Transfer Function.py
Question: Plot the Bode plot for a transfer function 
𝐻(𝑠)=1/𝑠^2+2𝑠+1

'''

import control as ctrl
import matplotlib.pyplot as plt
import numpy as np

# Define the transfer function H(s) = 1 / (s^2 + 2s + 1)
num = [1]
den = [1, 2, 1]
H = ctrl.TransferFunction(num, den,)

# Plot the Bode plot
# By setting plot=False, we tell the function to return the data instead of plotting it
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

'''
Traceback (most recent call last):
  File "/home/dora/Electrical_ENGINEERING/Sample Question 4: Bode Plot of a Transfer Function.py", line 17, in <module>
    mag, phase, omega = ctrl.bode(H, dB=True)
    ^^^^^^^^^^^^^^^^^
ValueError: not enough values to unpack (expected 3, got 2)
[Finished in 1.6s]
'''