from sympy import symbols, laplace_transform, Heaviside, inverse_laplace_transform, cos, sin, exp

# Define the symbols
t, s = symbols('t s')

# Define a function involving Heaviside functions
f = -t**2*Heaviside(t - 3) + cos(t)*Heaviside(t - 5)

# Compute the Laplace transform of f(t)
F = laplace_transform(f, t, s)
print("Laplace transform of f(t):", F[0])

# Define another function with piecewise definitions
h = t**4 + 3*sin((t - 5)/10)*Heaviside(t - 5)

# Compute the Laplace transform of h(t)
H = laplace_transform(h, t, s)
print("Laplace transform of h(t):", H[0])

# Define a more complex function involving shifts and exponentials
g = 10*Heaviside(t - 12) + 2*(t - 6)**3*Heaviside(t - 6) - (7 - exp(-12 - 3*t))*Heaviside(t - 4)

# Compute the Laplace transform of g(t)
G = laplace_transform(g, t, s)
print("Laplace transform of g(t):", G[0])

# Compute inverse Laplace transforms
inverse_F = inverse_laplace_transform(F[0], s, t)
print("Inverse Laplace transform of F(s):", inverse_F.simplify())

inverse_H = inverse_laplace_transform(H[0], s, t)
print("Inverse Laplace transform of H(s):", inverse_H.simplify())

inverse_G = inverse_laplace_transform(G[0], s, t)
print("Inverse Laplace transform of G(s):", inverse_G.simplify())