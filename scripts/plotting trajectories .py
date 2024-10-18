import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the system of differential equations
def system_of_odes(x, t):
    # Define the matrix A
    A = np.array([[1, 2], [3, 2]])
    # Calculate dx/dt = A * x
    dxdt = np.dot(A, x)
    return dxdt

# Time points for plotting
t = np.linspace(0, 5, 500)

# Initial conditions for trajectories
initial_conditions = [
    np.array([1, 0]),   # Example 1: starting at (1, 0)
    np.array([0, 1]),   # Example 2: starting at (0, 1)
    np.array([-1, 2])   # Example 3: starting at (-1, 2)
]

# Solve the differential equations for each initial condition
solutions = [odeint(system_of_odes, ic, t) for ic in initial_conditions]

# Plotting the trajectories
plt.figure(figsize=(8, 6))
for sol, ic in zip(solutions, initial_conditions):
    plt.plot(sol[:, 0], sol[:, 1], label=f'Initial Condition: ({ic[0]}, {ic[1]})')

plt.title('Trajectories of the System: dx1/dt = x1 + 2*x2, dx2/dt = 3*x1 + 2*x2')
plt.xlabel('x1')
plt.ylabel('x2')
plt.grid(True)
plt.legend()
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlim([-3, 3])
plt.ylim([-3, 3])
plt.show()