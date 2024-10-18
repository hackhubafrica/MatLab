
from sympy import symbols, Function, dsolve, Eq, Derivative ,exp


# Define the symbol for t
t = symbols('t')

# Define the function y(t)
y = Function('y')
# Define the differential equation for Example 2
ode2 = Eq(2*y(t).diff(t, 2) + 3*y(t).diff(t) - 2*y(t), t*exp(-2*t))
print(ode2)

# Define the initial conditions
initial_conditions2 = {y(0): 0, y(t).diff(t).subs(t, 0): -2}

# Solve the ODE for Example 2
solution2 = dsolve(ode2, y(t), ics=initial_conditions2)

# Print the solution
print("\nSolution to Example 2:")
print(solution2)


'''
Traceback (most recent call last):
  File "/home/dora/Electrical_ENGINEERING/#problems (IVPs)EX2.py", line 11, in <module>
    ode2 = Eq(2*y(t).diff(t, 2) + 3*y(t).diff(t) - 2*y(t), t*exp(-2*t))
                                                             ^^^
NameError: name 'exp' is not defined
[Finished in 580ms with exit code 1]
[cmd: ['python3', '-u', '/home/dora/Electrical_ENGINEERING/#problems (IVPs)EX2.py']]
[dir: /home/dora/Electrical_ENGINEERING]
[path: /usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/var/lib/snapd/snap/bin]
'''