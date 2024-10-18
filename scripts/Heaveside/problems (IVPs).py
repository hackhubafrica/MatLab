from sympy import symbols, Function, dsolve, Eq, Derivative

# Define the symbol for t
t = symbols('t')

# Define the function y(t)
y = Function('y')

# Define the differential equation
ode = Eq(y(t).diff(t, 2) - 10*y(t).diff(t) + 9*y(t), 5*t)

# Define the initial conditions
initial_conditions = {y(0): -1, y(t).diff(t).subs(t, 0): 2}

# Solve the ODE
solution = dsolve(ode, y(t), ics=initial_conditions)

# Print the solution
print("Solution to Example 1:")
print(solution)