from sympy import symbols, Function, exp, Heaviside, cos, Eq, dsolve

# Define symbols and functions
t = symbols('t')
y = Function('y')
u2 = Heaviside(t - 2)

# Define the ODE
ode1 = Eq(y(t).diff(t, 2) - y(t).diff(t) + 5*y(t), 4 + u2*exp(4-2*t))

# Define initial conditions
initial_conditions1 = {y(0): 2, y(t).diff(t).subs(t, 0): -1}

# Solve the ODE
solution1 = dsolve(ode1, y(t), ics=initial_conditions1)
print("Solution to Example 1:")
print(solution1)