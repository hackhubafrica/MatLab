from simple_pid import PID
import numpy as np
import matplotlib.pyplot as plt

# PID controller setup (tune Kp, Ki, Kd for your system)
pid = PID(1.0, 0.1, 0.05, setpoint=0)  # Proportional, Integral, Derivative constants
pid.output_limits = (-5, 5)  # Motor speed range (degrees per second)

# Motor and panel parameters
panel_azimuth = 0.0  # Initial azimuth of the panel (degrees)

# Simulation parameters
time_step = 0.1  # Time step (seconds)
total_time = 20  # Total simulation time (seconds)

# Store data for plotting
times = []
panel_azimuths = []
sun_azimuths = []

# Simulate the movement over time
for t in np.arange(0, total_time, time_step):
    # Example: Sun's azimuth changes over time
    sun_azimuth = 30 + 1.5 * t  # Sun's azimuth (degrees)

    # Compute the error (difference between the panel and sun's azimuth)
    pid.setpoint = sun_azimuth
    control_signal = pid(panel_azimuth)  # Get PID output for motor control

    # Update panel azimuth (adjusting based on motor speed)
    panel_azimuth += control_signal * time_step

    # Record for plotting
    times.append(t)
    panel_azimuths.append(panel_azimuth)
    sun_azimuths.append(sun_azimuth)

    print(f"Time: {t:.1f}s, Panel Azimuth: {panel_azimuth:.2f}, Sun Azimuth: {sun_azimuth:.2f}, Control: {control_signal:.2f}")

# Plot the result
plt.plot(times, panel_azimuths, label="Panel Azimuth")
plt.plot(times, sun_azimuths, label="Sun Azimuth", linestyle="--")
plt.xlabel("Time (s)")
plt.ylabel("Azimuth (degrees)")
plt.legend()
plt.show()
