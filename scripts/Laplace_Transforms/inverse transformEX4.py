import sympy as sp

# Define variables
t, s = sp.symbols('t s')

# Define the function
G = 8 / (3*(s**2 + 12)) + (3*s**2 - 49) / (s**2 + 12)

# Compute the inverse Laplace transform
g = sp.inverse_laplace_transform(G, s, t)

print(g)