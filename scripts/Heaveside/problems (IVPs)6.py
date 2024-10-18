from sympy import symbols, Function, exp, Heaviside, cos, Eq, dsolve

# Define symbols and functions
t = symbols('t')
y = Function('y')
u2 = Heaviside(t - 2)
u6 = Heaviside(t - 6)
u3 = Heaviside(t - 3)
u1 = Heaviside(t - 1)

# Define the ODE
ode3 = Eq(y(t).diff(t, 2) - 5*y(t).diff(t) - 14*y(t), 9 + u3 + 4*(t - 1)*u1)

# Define initial conditions
initial_conditions3 = {y(0): 0, y(t).diff(t).subs(t, 0): 10}

# Solve the ODE
solution3 = dsolve(ode3, y(t), ics=initial_conditions3)
print("\nSolution to Example 3:")
print(solution3)