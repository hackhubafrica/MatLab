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

# MPC setup
Ts = 0.1  # Sampling time
p = 10    # Prediction horizon

# Create MPC controller
controller = ctrl.MPC(sys_ss, Ts, p)

# Simulate step response
t = np.arange(0, 10, Ts)
t_input = np.ones_like(t)  # Step input
t_output, y_output, x_output = ctrl.forced_response(controller, T=t, U=t_input)

# Plot the response
plt.figure(figsize=(10, 6))
plt.plot(t_output, y_output, label='Output')
plt.title('Step Response of MPC Controlled DC Motor')
plt.xlabel('Time (s)')
plt.ylabel('Output')
plt.grid(True)
plt.legend()
plt.show()


'''
Traceback (most recent call last):
  File "/home/dora/Electrical_ENGINEERING/scripts/Model Predictive Control (MPC).py", line 19, in <module>
    controller = ctrl.MPC(sys_ss, Ts, p)
                 ^^^^^^^^
AttributeError: module 'control' has no attribute 'MPC'
plt.show()
[Finished in 1.4s]
'''