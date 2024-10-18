import numpy
import sympy
from sympy import symbols, Function, dsolve, Eq, Derivative


# Define the symbol for t
t = symbols('t')

# Define the function y(t)
y = Function('y')

# Define the differential equation for Example 4
ode4 = Eq(y(t).diff(t, 2) + 4*y(t).diff(t), cos(t-3) + 4*t)

# Define the initial conditions
initial_conditions4 = {y(3): 0, y(t).diff(t).subs(t, 3): 7}

# Solve the ODE for Example 4
solution4 = dsolve(ode4, y(t), ics=initial_conditions4)

# Print the solution
print("\nSolution to Example 4:")
print(solution4)

'''
Traceback (most recent call last):
  File "/home/dora/Electrical_ENGINEERING/#problems (IVPs)EX4.py", line 13, in <module>
    ode4 = Eq(y(t).diff(t, 2) + 4*y(t).diff(t), cos(t-3) + 4*t)
                                                ^^^
NameError: name 'cos' is not defined
[Finished in 695ms with exit code 1]
[cmd: ['python3', '-u', '/home/dora/Electrical_ENGINEERING/#problems (IVPs)EX4.py']]
[dir: /home/dora/Electrical_ENGINEERING]
[path: /usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/var/lib/snapd/snap/bin]
'''