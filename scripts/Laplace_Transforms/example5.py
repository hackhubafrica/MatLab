import sympy as sp

#f(t)=(10t)**3/2
# Define variables
t, s = sp.symbols('t s')
# Define the function

f = (10*t)**(3/2)

# Compute the Laplace transform
F = sp.laplace_transform(f, t, s)

print(F)

'''
Result:

G(s)= Γ(5/2)/s**5/2 
'''