
from sympy import symbols, Function, dsolve, Eq, Derivative


# Define the symbol for t
t = symbols('t')

# Define the function y(t)
y = Function('y')

# Define the differential equation for Example 3
ode3 = Eq(y(t).diff(t, 2) - 6*y(t).diff(t) + 15*y(t), 2*sin(3*t))

# Define the initial conditions
initial_conditions3 = {y(0): -1, y(t).diff(t).subs(t, 0): -4}

# Solve the ODE for Example 3
solution3 = dsolve(ode3, y(t), ics=initial_conditions3)

# Print the solution
print("\nSolution to Example 3:")
print(solution3)

'''
Traceback (most recent call last):
  File "/home/dora/Electrical_ENGINEERING/#problems (IVPs)EX3.py", line 12, in <module>
    ode3 = Eq(y(t).diff(t, 2) - 6*y(t).diff(t) + 15*y(t), 2*sin(3*t))
                                                            ^^^
NameError: name 'sin' is not defined. Did you mean: 'bin'?
[Finished in 573ms with exit code 1]
[cmd: ['python3', '-u', '/home/dora/Electrical_ENGINEERING/#problems (IVPs)EX3.py']]
[dir: /home/dora/Electrical_ENGINEERING]
[path: /usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/var/lib/snapd/snap/bin]
'''