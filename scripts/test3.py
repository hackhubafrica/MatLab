import numpy as np
import matplotlib.pyplot as plt
import skrf as rf

# Define the transmission line parameters
Z0 = 50  # Characteristic impedance in ohms
ZL = 75 + 25j  # Load impedance

# Define frequency range
freq = rf.Frequency(1, 10, 101, 'ghz')

# Create a one-port network representing the load impedance
network = rf.Network(frequency=freq, z0=Z0)

# Define the load impedance in terms of its reflection coefficient
gamma = (ZL - Z0) / (ZL + Z0)

# Set the network's reflection coefficient (s-parameter)
network.s = gamma

# Plot the Smith chart
plt.figure()
network.plot_s_smith()
plt.title('Smith Chart for Impedance Matching')
plt.show()
