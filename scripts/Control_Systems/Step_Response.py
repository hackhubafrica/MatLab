import numpy as np
import control as ctrl
import matplotlib.pyplot as plt


# Define the transfer function H(s) = 1 / (s^2 + 2s + 1)
num = [1]
den = [1, 2, 1]
H = ctrl.TransferFunction(num, den)

# Define the transfer function G(s) = 1 / (s^2 + s)  OR G(s) = 1 / s(s + 1)
num = [1]
den = [1, 1, 0]
G = ctrl.TransferFunction(num, den)

# Define the transfer function D(s) = s / (s + 1)
num = [1,0]
den = [0, 1, 1]
D = ctrl.TransferFunction(num, den)


# # Compute the final value
# final_value = y[-1]
# print(final_value)

# # Compute Rise Time (time to go from 10% to 90% of final value)
# rise_time_start = np.where(y >= 0.1 * final_value)[0][0]
# rise_time_end = np.where(y >= 0.9 * final_value)[0][0]
# rise_time = t[rise_time_end] - t[rise_time_start]

# # Compute Overshoot (maximum value over final value)
# overshoot = (np.max(y) - final_value) / final_value * 100

# # Compute Settling Time (time to remain within 2% of final value)
# settling_time_idx = np.where(np.abs(y - final_value) <= 0.02 * final_value)[0]
# if len(settling_time_idx) > 0:
#     settling_time = t[settling_time_idx[-1]]
# else:
#     settling_time = t[-1]  # Fallback to last time if not settled

# # Compute Steady-State Error (difference from 1)
# steady_state_error = 1 - final_value

# # Print the calculated values
# print(f"Rise Time: {rise_time:.4f} seconds")
# print(f"Overshoot: {overshoot:.2f}%")
# print(f"Settling Time: {settling_time:.4f} seconds")
# print(f"Steady-State Error: {steady_state_error:.4f}")


t = np.linspace(0,20,100)
# Compute the step response
t, y = ctrl.step_response(H,T=t)

x = ctrl.step_info(H)
print(x)

# Plot the response
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Step Response Of a low pass filter')
plt.grid(True)
plt.show()


t, y = ctrl.step_response(G,T=t)
x = ctrl.step_info(G)
print(x)

# Plot the response
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Step Response of a Type 1 Transer Function')
plt.grid(True)
plt.show()


t, y = ctrl.step_response(D,T=t)
x = ctrl.step_info(D)
print(x)

# Plot the response
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Step Response of a High pass filter')
plt.grid(True)
plt.show()

# forced_response, initial_response, step_response
