import sympy as sp

#f(t)=6e^−5t +e^3t +5t**3 −9
# Define variables
t, s = sp.symbols('t s')

# Define the function
f = 6*sp.exp(-5*t) + sp.exp(3*t) + 5*t**3 - 9

# Compute the Laplace transform
F = sp.laplace_transform(f, t, s)
print(F)