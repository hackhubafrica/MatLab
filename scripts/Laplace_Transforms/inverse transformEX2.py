import sympy as sp

# Define variables
t, s = sp.symbols('t s')

# Define the function
H = (19*s + 2) / (3*(s - 5)) + 7 / (s**5)

# Compute the inverse Laplace transform
h = sp.inverse_laplace_transform(H, s, t)
print(h)