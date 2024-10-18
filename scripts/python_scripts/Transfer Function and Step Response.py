import control as ctrl
import matplotlib.pyplot as plt

# Define the transfer function H(s) = 1 / (s^2 + 2s + 1)
num = [1]
den = [1, 2, 1]
H = ctrl.TransferFunction(num, den)

# Compute the step response
t, y = ctrl.step_response(H)

# Plot the response
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Step Response')
plt.grid(True)
plt.show()
