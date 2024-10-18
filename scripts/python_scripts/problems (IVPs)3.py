from sympy import symbols, Function, dsolve, Eq, Derivative,sin, cos, exp
import sympy
# Define the symbol for t
t = symbols('t')

# Define the function y(t)
y = Function('y')

# Define the differential equation
ode3 = Eq(y(t).diff(t, 2) - 6*y(t).diff(t) + 15*y(t), 2*sin(3*t))

# Define the initial conditions
initial_conditions3 = {y(0): -1, y(t).diff(t).subs(t, 0): -4}

# Solve the ODE for Example 3
solution3 = dsolve(ode3, y(t), ics=initial_conditions3)

# Print the solution
print("\nSolution to Example 3:")
print(solution3)