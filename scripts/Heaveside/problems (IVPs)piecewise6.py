from sympy import symbols, Function, exp, Heaviside, cos, Eq, dsolve

# Define symbols and functions
t = symbols('t')
y = Function('y')
u2 = Heaviside(t - 2)
u6 = Heaviside(t - 6)
u3 = Heaviside(t - 3)
u1 = Heaviside(t - 1)
g = Piecewise((2, t < 6), (t, t < 10), (4*t, t >= 10))

# Define the ODE
ode4 = Eq(y(t).diff(t, 2) + 3*y(t).diff(t) + 2*y(t), g)

# Define initial conditions
initial_conditions4 = {y(0): 0, y(t).diff(t).subs(t, 0): -2}

# Solve the ODE
solution4 = dsolve(ode4, y(t), ics=initial_conditions4)
print("\nSolution to Example 4:")
print(solution4)