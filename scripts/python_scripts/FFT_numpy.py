import numpy as np
import matplotlib.pyplot as plt

N = 500
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = np.fft.fft(y)
xf = np.fft.fftfreq(N, T)[:N//2]

plt.plot(xf, 2.0/N * np.abs(yf[:N//2]))
plt.grid()
plt.show()