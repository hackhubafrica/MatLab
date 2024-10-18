import control as ctrl
import matplotlib.pyplot as plt

# Define the transfer function H(s) = 1 / (s^2 + 2s + 1)
num = [1]
den = [1, 2, 1]
H = ctrl.TransferFunction(num, den)

# Plot the root locus
ctrl.root_locus(H)
plt.show()
