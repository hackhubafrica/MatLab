#Example: FFT for Signal Analysis

import numpy as np
import matplotlib.pyplot as plt

# Sample signal
t = np.linspace(0, 1, 1000, endpoint=False)
signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)

# Fourier transform
fft_result = np.fft.fft(signal)
fft_freq = np.fft.fftfreq(len(t), 1 / 1000)

# Plot the FFT result
plt.plot(fft_freq, np.abs(fft_result))
plt.title('FFT of Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()