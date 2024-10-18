import sympy as sp

# f(t)=tg′(t)
# Define variables
#To find f(t)=tg′(t), we need to differentiate g(t) first.

t, s = sp.symbols('t s')
# Define the function
# Define g'(t)

g_prime = sp.diff(g, t)

# Define f(t) = t * g'(t)
f = t * g_prime

# Compute the Laplace transform
F = sp.laplace_transform(f, t, s)
print(F)

