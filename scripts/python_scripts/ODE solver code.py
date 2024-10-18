from sympy import symbols, Function, Eq, dsolve, sin, cos, exp

# Define the symbols
t = symbols('t')
y = Function('y')

# Example 1: Solving y'' + 3*t*y' - 6*y = 2 with initial conditions y(0) = 0, y'(0) = 0
ode1 = Eq(y(t).diff(t, 2) + 3*t*y(t).diff(t) - 6*y(t), 2)
initial_conditions1 = {y(0): 0, y(t).diff(t).subs(t, 0): 0}
solution1 = dsolve(ode1, y(t), ics=initial_conditions1)
print("Solution to Example 1:")
print(solution1)

# Example 2: Solving t*y'' - t*y' + y = 2 with initial conditions y(0) = 2, y'(0) = -4
ode2 = Eq(t*y(t).diff(t, 2) - t*y(t).diff(t) + y(t), 2)
initial_conditions2 = {y(0): 2, y(t).diff(t).subs(t, 0): -4}
solution2 = dsolve(ode2, y(t), ics=initial_conditions2)
print("\nSolution to Example 2:")
print(solution2)


'''
Traceback (most recent call last):
  File "/home/dora/Electrical_ENGINEERING/scripts/ODE solver code.py", line 10, in <module>
    solution1 = dsolve(ode1, y(t), ics=initial_conditions1)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dora/.local/lib/python3.12/site-packages/sympy/solvers/ode/ode.py", line 640, in dsolve
    return _helper_simplify(eq, hint, hints, simplify, ics=ics)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dora/.local/lib/python3.12/site-packages/sympy/solvers/ode/ode.py", line 670, in _helper_simplify
    sols = solvefunc.get_general_solution()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dora/.local/lib/python3.12/site-packages/sympy/solvers/ode/single.py", line 283, in get_general_solution
    return self._get_general_solution(simplify_flag=simplify)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dora/.local/lib/python3.12/site-packages/sympy/solvers/ode/single.py", line 907, in _get_general_solution
    raise NotImplementedError("The given ODE " + str(eq) + " cannot be solved by"
NotImplementedError: The given ODE Derivative(y(t), t) - (6*y(t) - Derivative(y(t), (t, 2)) + 2)/(3*t) cannot be solved by the factorable group method
[Finished in 1.6s with exit code 1]
[cmd: ['python3', '-u', '/home/dora/Electrical_ENGINEERING/scripts/ODE solver code.py']]
[dir: /home/dora/Electrical_ENGINEERING/scripts]
[path: /usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/var/lib/snapd/snap/bin]
'''