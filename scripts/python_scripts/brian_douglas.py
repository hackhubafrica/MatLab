import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import control as ctrl

# Define the continuous-time transfer function
num = [1, 2]        # Numerator: s + 2
den = [1, 1, 2]     # Denominator: s^2 + s + 2
system = ctrl.TransferFunction(num, den)

# Visualize the continuous-time step response
time, response = ctrl.step_response(system)

plt.figure()
plt.plot(time, response, label='Continuous-Time Response')
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.title('Step Response')
plt.grid(True)
# plt.show()

# Define different sampling times
sampling_times = [0.1, 0.5, 1.0]  # in seconds

for Ts in sampling_times:
    # Convert the continuous-time system to discrete-time (using zero-order hold method)
    discrete_system = ctrl.sample_system(system, Ts, method='zoh')

    # Simulate the discrete-time step response
    time_discrete, response_discrete = ctrl.step_response(discrete_system)

    # Plot the discrete-time response
    plt.plot(time_discrete, response_discrete, label=f'Discrete-Time Ts={Ts}s')

# Add legend and show plot
plt.legend()
plt.show()
