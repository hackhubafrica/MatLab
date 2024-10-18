from sympy import inverse_laplace_transform
import sympy as sp
# Define the function F(s)

t, s = sp.symbols('t s')
F_s = (2*s + 3) / ((s + 1) * (s + 2))

# Compute inverse Laplace transform
f_t = inverse_laplace_transform(F_s, s, t)
print(f_t)