import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Define the plant transfer function (system to be controlled)
plant = ctrl.TransferFunction([1], [1, 2, 1])

# PID controller parameters
Kp = 1.2   # Proportional gain
Ki = 1.0   # Integral gain
Kd = 0.2   # Derivative gain

# Create PID controller
controller = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])

# Feedback loop (closed-loop system)
system = ctrl.feedback(plant * controller)

# Time vector for simulation
t = np.linspace(0, 10, 1000)

# Step input (unit step)
t_input = np.ones_like(t)

# Simulate response
t_output, y_output = ctrl.forced_response(system, T=t, U=t_input)

# Plot the response
plt.figure(figsize=(10, 6))
plt.plot(t_output, y_output, label='Output')
plt.title('Step Response of PID Controller')
plt.xlabel('Time (s)')
plt.ylabel('Output')
plt.grid(True)
plt.legend()
plt.show()