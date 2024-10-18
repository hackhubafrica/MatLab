from sympy import symbols, Function, laplace_transform, inverse_laplace_transform, exp, sin

# Define symbols
s, t = symbols('s t')
Y = Function('Y')(s)

# Define the Laplace transform of g(t)
G_s = 1 / (s**2)  # Replace with actual Laplace transform of g(t)

# Define the ODE in terms of Y(s)
ode = 4*s**2*Y + Y - 4*3*s + 7
solution_Y = Y(s).solve(ode,Y(s))