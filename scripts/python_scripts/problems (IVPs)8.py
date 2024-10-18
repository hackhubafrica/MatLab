from sympy import symbols, Function, DiracDelta, Heaviside, Eq, dsolve

# Define symbols and functions
t = symbols('t')
y = Function('y')
delta_func = DiracDelta(t - 9)
# Define Heaviside function for step function u12(t)
u12 = Heaviside(t - 12)
delta_func2 = DiracDelta(t - 4)

# Define the ODE
ode2 = Eq(2*y(t).diff(t, 2) + 10*y(t), 3*u12 - 5*delta_func2)

# Define initial conditions
initial_conditions2 = {y(0): -1, y(t).diff(t).subs(t, 0): -2}

# Solve the ODE
solution2 = dsolve(ode2, y(t), ics=initial_conditions2)
print("\nSolution to Example 2:")
print(solution2)