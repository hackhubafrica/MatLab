'''
Example 2: Nyquist Plot of a Transfer Function.py
Question: Plot the Nyquist plot for a transfer function 
𝐻(𝑠)=10/𝑠(𝑠+2)(𝑠+5)

Solution:
'''

import control as ctrl
import matplotlib.pyplot as plt

# Define the transfer function H(s) = 10 / (s(s+2)(s+5))
num = [10]
den = [1, 7, 10, 0]
H = ctrl.TransferFunction(num, den)

# Plot the Nyquist plot
ctrl.nyquist(H)
plt.title('Nyquist Plot')
plt.grid(True)
plt.show()