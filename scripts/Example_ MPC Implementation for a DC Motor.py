import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Define system matrices (example: DC motor)
A = np.array([[0, 1], [-1, -0.1]])
B = np.array([[0], [1]])
C = np.array([[1, 0]])
D = np.array([[0]])

# Create state-space model
sys_ss = ctrl.StateSpace(A, B, C, D)

# MPC parameters
Ts = 0.1   # Sampling time
p = 10     # Prediction horizon
m = 1      # Control horizon

# Create MPC controller
controller = ctrl.MPC(sys_ss, Ts, p, m)

# Simulation setup
t = np.arange(0, 10, Ts)  # Time vector
U = np.ones((1, len(t)))  # Step input (unit step)

# Simulate MPC controlled system
t_output, y_output, x_output = ctrl.forced_response(controller, T=t, U=U)

# Plot the response
plt.figure(figsize=(10, 6))
plt.plot(t_output, y_output, label='Output')
plt.title('MPC Controlled DC Motor Response')
plt.xlabel('Time (s)')
plt.ylabel('Output')
plt.grid(True)
plt.legend()
plt.show()