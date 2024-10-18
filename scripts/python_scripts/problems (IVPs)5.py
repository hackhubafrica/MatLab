from sympy import symbols, Function, exp, Heaviside, cos, Eq, dsolve

# Define symbols and functions
t = symbols('t')
y = Function('y')
u2 = Heaviside(t - 2)
u6 = Heaviside(t - 6)

# Define the ODE
ode2 = Eq(y(t).diff(t, 2) - y(t).diff(t), cos(2*t) + cos(2*t - 12)*u6)

# Define initial conditions
initial_conditions2 = {y(0): -4, y(t).diff(t).subs(t, 0): 0}

# Solve the ODE
solution2 = dsolve(ode2, y(t), ics=initial_conditions2)
print("\nSolution to Example 2:")
print(solution2)