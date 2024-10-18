import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Define system matrices (example inverted pendulum)
A = np.array([[0, 1], [0, -0.1]])
B = np.array([[0], [1]])
C = np.array([[1, 0]])
D = np.array([[0]])

# Create state-space model
sys_ss = ctrl.StateSpace(A, B, C, D)

# Design LQR controller
Q = np.diag([1, 1])  # State weighting matrix
R = np.diag([0.01])  # Control input weighting matrix
K, S, E = ctrl.lqr(sys_ss, Q, R)

# Closed-loop system
sys_cl = ctrl.StateSpace(A - B @ K, B, C, D)

# Simulate step response
t = np.linspace(0, 10, 1000)
t_input = np.ones_like(t)  # Step input
t_output, y_output, x_output = ctrl.forced_response(sys_cl, T=t, U=t_input)

# Plot the response
plt.figure(figsize=(10, 6))
plt.plot(t_output, y_output, label='Output')
plt.title('Step Response of LQR Controlled Inverted Pendulum')
plt.xlabel('Time (s)')
plt.ylabel('Output')
plt.grid(True)
plt.legend()
plt.show()