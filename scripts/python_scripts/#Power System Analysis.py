#Example: Load Flow Analysis

import numpy as np

# Admittance matrix (Y-bus)
Y_bus = np.array([[10-5j, -5+2j], [-5+2j, 5-2j]])

# Bus voltages (initial guess)
V = np.array([1+0j, 1+0j])

# Load power (P-Q) at each bus
S = np.array([0, -2-1j])

# Newton-Raphson method for load flow analysis
def load_flow(Y_bus, V, S, tol=1e-6, max_iter=10):
    for _ in range(max_iter):
        I = np.dot(Y_bus, V)
        S_calculated = V * np.conj(I)
        mismatch = S - S_calculated[1:]
        if np.all(np.abs(mismatch) < tol):
            break
        dV = np.linalg.solve(Y_bus[1:, 1:], mismatch / np.conj(V[1:]))
        V[1:] += dV
    return V

V_solution = load_flow(Y_bus, V, S)
print(f"Bus Voltages: {V_solution}")

'''
Traceback (most recent call last):
  File "/home/dora/Electrical_ENGINEERING/Power System Analysis.py", line 26, in <module>
    V_solution = load_flow(Y_bus, V, S)
                 ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dora/Electrical_ENGINEERING/Power System Analysis.py", line 22, in load_flow
    dV = np.linalg.solve(Y_bus[1:, 1:], mismatch / np.conj(V[1:]))
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/dora/.local/lib/python3.12/site-packages/numpy/linalg/_linalg.py", line 410, in solve
    r = gufunc(a, b, signature=signature)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: solve1: Input operand 1 has a mismatch in its core dimension 0, with gufunc signature (m,m),(m)->(m) (size 2 is different from 1)
[Finished in 222ms with exit code 1]
[cmd: ['python3', '-u', '/home/dora/Electrical_ENGINEERING/Power System Analysis.py']]
[dir: /home/dora/Electrical_ENGINEERING]
[path: /usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/var/lib/snapd/snap/bin]
'''