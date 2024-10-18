from sympy import inverse_laplace_transform,laplace_transform,sin, cos
import sympy as sp

# Define the function F(s)

t, s = sp.symbols('t s')
# Define the function f(t)
from sympy import sin, cos

f_t = sin(3*t)

# Compute the Laplace transform of f(t)
F_s = laplace_transform(f_t, t, s)[0]

# Compute the derivative of f(t)
f_prime_t = f_t.diff(t)

# Compute the Laplace transform of f'(t)
F_prime_s = laplace_transform(f_prime_t, t, s)[0]

F_s, F_prime_s
print(F_s)
print(F_prime_s)