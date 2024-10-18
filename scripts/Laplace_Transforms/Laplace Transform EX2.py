from sympy import symbols, exp, factorial, integrate, laplace_transform, inverse_laplace_transform,Heaviside
from sympy.abc import t, s, a

# Define symbols
t, s, a, n = symbols('t s a n', positive=True, real=True, constant=True)

# Define the function e^{-2t} * u(t-2)
f_t = exp(-2*t) * Heaviside(t-2)

# Compute Laplace transform
F_s = laplace_transform(f_t, t, s)
print(F_s)