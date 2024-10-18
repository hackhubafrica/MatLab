# Define the function
import sympy as sp

#g(t)=4cos(4t)−9sin(4t)+2cos(10t)

t, s = sp.symbols('t s')
g = 4*sp.cos(4*t) - 9*sp.sin(4*t) + 2*sp.cos(10*t)

# Compute the Laplace transform
G = sp.laplace_transform(g, t, s)
print(G)