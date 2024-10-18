from scipy.fft import fft, fftfreq
import numpy as np
import matplotlib.pyplot as plt
# Sample signal
t = np.linspace(0, 1, 1000, endpoint=False)
signal = np.sin(2*np.pi*50*t) + np.sin(2*np.pi*120*t)


# Fourier transform
yf = fft(signal)
xf = fftfreq(len(t), 1/1000)

# Plot the FFT
plt.plot(xf, np.abs(yf))
plt.title('FFT of Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
