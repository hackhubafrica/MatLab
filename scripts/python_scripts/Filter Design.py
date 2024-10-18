#Example: Butterworth Lowpass Filter Design

import numpy as np
from scipy.signal import butter, freqz
import matplotlib.pyplot as plt

# Filter specifications
order = 4
cutoff = 1000  # Cutoff frequency in Hz
fs = 8000  # Sampling frequency in Hz

# Butterworth filter design
b, a = butter(order, cutoff / (0.5 * fs), btype='low', analog=False)

# Frequency response
w, h = freqz(b, a, worN=8000)

# Plot the frequency response
plt.plot(0.5 * fs * w / np.pi, np.abs(h), 'b')
plt.title('Butterworth Lowpass Filter Frequency Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain')
plt.grid()
plt.show()