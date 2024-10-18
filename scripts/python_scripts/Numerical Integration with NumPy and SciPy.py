import numpy as np
from scipy.integrate import quad

def integrand(x):
    return np.sin(x)**2

result, error = quad(integrand, 0, np.pi)
print(f"Integral result: {result} with error: {error}")
