from sympy import symbols, Function, DiracDelta, Heaviside, Eq, dsolve

# Define symbols and functions
t = symbols('t')
y = Function('y')
delta_func = DiracDelta(t - 9)

# Define the ODE
ode1 = Eq(y(t).diff(t, 2) + 2*y(t).diff(t) - 15*y(t), 6*delta_func)

# Define initial conditions
initial_conditions1 = {y(0): -5, y(t).diff(t).subs(t, 0): 7}

# Solve the ODE
solution1 = dsolve(ode1, y(t), ics=initial_conditions1)
print("Solution to Example 1:")
print(solution1)