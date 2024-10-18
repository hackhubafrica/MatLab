import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Define the PID controller transfer function
Kp = 1
Ki = 0.5
Kd = 0.2

numerator = [Kd, Kp, Ki]
denominator = [1, 0]
C = ctrl.TransferFunction(numerator, denominator)

# Simulate step response
t, y = ctrl.step_response(C)

# Plot the step response
plt.plot(t, y)
plt.title('Step Response of PID Controller')
plt.xlabel('Time (s)')
plt.ylabel('Output')
plt.grid()
plt.show()