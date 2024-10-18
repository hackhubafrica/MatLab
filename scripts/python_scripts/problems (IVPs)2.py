from sympy import symbols, Function, dsolve, Eq, Derivative,exp

# Define the symbol for t
t = symbols('t')

# Define the function y(t)
y = Function('y')

# Define the differential equation
ode2 = Eq(2*y(t).diff(t, 2) + 3*y(t).diff(t) - 2*y(t), t*exp(-2*t))

# Define the initial conditions
initial_conditions2 = {y(0): 0, y(t).diff(t).subs(t, 0): -2}

# Solve the ODE for Example 2
solution2 = dsolve(ode2, y(t), ics=initial_conditions2)

# Print the solution
print("\nSolution to Example 2:")
print(solution2)