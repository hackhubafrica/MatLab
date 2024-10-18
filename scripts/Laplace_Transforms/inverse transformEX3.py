import sympy as sp

# Define variables
t, s = sp.symbols('t s')

# Define the function
F = 6*s / (s**2 + 25) + 3*s**2 / (s**2 + 25)

# Compute the inverse Laplace transform
f = sp.inverse_laplace_transform(F, s, t)
print(f)