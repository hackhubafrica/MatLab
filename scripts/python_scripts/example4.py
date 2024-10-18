import sympy as sp

#g(t)=t**3/2
# Define variables
t, s = sp.symbols('t s')
# Define the function
g = t**(3/2)

# Compute the Laplace transform
G = sp.laplace_transform(g, t, s)
print(G)

'''
Result:

G(s)= Γ(5/2)/s**5/2 
'''