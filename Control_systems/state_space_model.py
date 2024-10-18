import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm

# System matrices (continuous-time)
A = np.array([[0, 1],
              [-2, -1]])
B = np.array([[0],
              [1]])
C = np.array([[1, 0]])
D = np.array([[0]])

# Discretization parameters
dt = 0.1  # Sampling time (change to see effect on accuracy)
total_time = 10
num_steps = int(total_time / dt)

# Discretize the system
Ad = expm(A * dt)
Bd = np.linalg.inv(A) @ (Ad - np.eye(2)) @ B

# Initialize state and input
x = np.array([[0], [0]])  # initial conditions: x1(0) = 0, x2(0) = 0
u = 1  # Step input

# Arrays to store results
x_trajectory = np.zeros((num_steps, 2))
y_trajectory = np.zeros(num_steps)

# Simulate the system in discrete time
for k in range(num_steps):
    # Record output
    y_trajectory[k] = C @ x
    
    # Update state
    x = Ad @ x + Bd * u
    
    # Record state
    x_trajectory[k, :] = x.T

# Plot results
time = np.linspace(0, total_time, num_steps)

plt.figure()
plt.plot(time, y_trajectory, label='Output (y)')
plt.xlabel('Time (s)')
plt.ylabel('y(t)')
plt.title('Discrete-Time Step Response')
plt.grid(True)
plt.legend()
plt.show()
