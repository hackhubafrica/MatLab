from sympy import symbols, exp, factorial, integrate, laplace_transform, inverse_laplace_transform
from sympy.abc import t, s, a

# Define symbols
t, s, a, n = symbols('t s a n', positive=True, real=True, constant=True)

# Define the function t^n * exp(-a*t)
f_t = t**n * exp(-a*t)
print(f_t)

# Compute Laplace transform
F_s = laplace_transform(f_t, t, s)
print(F_s)