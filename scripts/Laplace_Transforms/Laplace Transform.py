#Example: Laplace Transform and Inverse Transform with SymPy

import sympy as sp

# Define the variable and function
t, s = sp.symbols('t s')
f = sp.exp(-t) * sp.sin(t)
print('t =',t)
print('f =',f)

# Laplace Transform
F = sp.laplace_transform(f, t, s)
print(f"Laplace Transform: {F[0]}")

# Inverse Laplace Transform
f_inv = sp.inverse_laplace_transform(F[0], s, t)
print(f"Inverse Laplace Transform: {f_inv}")