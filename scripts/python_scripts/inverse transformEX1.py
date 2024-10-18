import sympy as sp

# Define variables
t, s = sp.symbols('t s')

# Define the function
F = (6*s - 1) / (s - 8) + 4 / (s - 3)

# Compute the inverse Laplace transform
f = sp.inverse_laplace_transform(F, s, t)
print(f)

'''
Result:
f(t)=6e^8t +4e^3t
'''