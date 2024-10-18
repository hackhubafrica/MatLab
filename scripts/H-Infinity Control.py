import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
import slycot

# Define system model (example: flexible structure)
A = np.array([[0, 1], [0.1, -0.05]])
B = np.array([[0], [1]])
C = np.array([[1, 0]])
D = np.array([[0]])

# Create state-space model
sys_ss = ctrl.StateSpace(A, B, C, D)

# Design H-Infinity controller
controller, _, _ = ctrl.hinfsyn(sys_ss, 1, 1)

# Closed-loop system
sys_cl = ctrl.feedback(sys_ss * controller)

# Simulate step response
t = np.linspace(0, 10, 1000)
t_input = np.ones_like(t)  # Step input
t_output, y_output = ctrl.step_response(sys_cl, T=t)

# Plot the response
plt.figure(figsize=(10, 6))
plt.plot(t_output, y_output, label='Output')
plt.title('Step Response of H-Infinity Controlled Flexible Structure')
plt.xlabel('Time (s)')
plt.ylabel('Output')
plt.grid(True)
plt.legend()
plt.show()

'''
slycot
'''