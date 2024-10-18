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
p = 20     # Prediction horizon
m = 5      # Control horizon

# Weighting matrices
Q = np.diag([1, 1])  # State weighting matrix
R = np.diag([0.01])  # Control input weighting matrix

# Create MPC controller
controller = ctrl.MPC(sys_ss, Ts, p, m, Q, R)

# Simulation setup
t = np.arange(0, 10, Ts)  # Time vector
U = np.ones((1, len(t)))  # Step input (unit step)

# Simulate MPC controlled system
t_output, y_output, x_output = ctrl.forced_response(controller, T=t, U=U)

# Calculate performance metrics
tracking_error = np.abs(y_output - U)
IAE = np.sum(np.abs(tracking_error)) * Ts  # Integrated Absolute Error

# Plot the response
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(t_output, y_output, label='Output')
plt.plot(t, U[0], 'k--', label='Reference')
plt.title('MPC Controlled System Response')
plt.xlabel('Time (s)')
plt.ylabel('Output')
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t_output, tracking_error, label='Tracking Error')
plt.title('Tracking Error')
plt.xlabel('Time (s)')
plt.ylabel('Error')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

print(f"Integrated Absolute Error (IAE): {IAE}")