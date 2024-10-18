# f(t)=sin(2t)cos(2t)
import sympy as sp

# Define the variable and function
t = sp.symbols('t')
f = sp.sin(2*t) * sp.cos(2*t)

# Compute the Laplace transform
F = sp.laplace_transform(f, t, sp)
F
