import control as ctrl
import matplotlib.pyplot as plt
import numpy as np

# Define the transfer function H(s) = 1 / (s^2 + 2s + 1)
num = [1]
den = [1, 2, 1]
H = ctrl.TransferFunction(num, den)

# Create a custom time vector from 0 to 20 seconds with 1000 points
t = np.linspace(0, 20, 1000)

# Compute the step response
t, y = ctrl.step_response(H,T=t)

# print(t,y)

# Compute the final value
final_value = y[-1]
print(final_value)

# Compute Rise Time (time to go from 10% to 90% of final value)
rise_time_start = np.where(y >= 0.1 * final_value)[0][0]
rise_time_end = np.where(y >= 0.9 * final_value)[0][0]
rise_time = t[rise_time_end] - t[rise_time_start]

# Compute Overshoot (maximum value over final value)
overshoot = (np.max(y) - final_value) / final_value * 100

# Compute Settling Time (time to remain within 2% of final value)
settling_time_idx = np.where(np.abs(y - final_value) <= 0.02 * final_value)[0]
if len(settling_time_idx) > 0:
    settling_time = t[settling_time_idx[-1]]
else:
    settling_time = t[-1]  # Fallback to last time if not settled

# Compute Steady-State Error (difference from 1)
steady_state_error = 1 - final_value

# Print the calculated values
print(f"Rise Time: {rise_time:.4f} seconds")
print(f"Overshoot: {overshoot:.2f}%")
print(f"Settling Time: {settling_time:.4f} seconds")
print(f"Steady-State Error: {steady_state_error:.4f}")


# Plot the response
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Step Response')
plt.grid(True)
plt.show()
