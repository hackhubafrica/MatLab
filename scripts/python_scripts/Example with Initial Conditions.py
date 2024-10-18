from sympy import symbols, Function, dsolve, Eq

# Define the symbol for t
t = symbols('t')

# Define the function y(t)
y = Function('y')

# Define the differential equation
ode = Eq(y(t).diff(t, 2) + 3*t*y(t).diff(t) - 6*y(t), 2)

# Define the initial conditions
initial_conditions = {y(0): 0, y(t).diff(t).subs(t, 0): 0}

# Solve the ODE with initial conditions
solution = dsolve(ode, y(t), ics=initial_conditions)

# Print the solution
print("Solution to the differential equation:")
print(solution)