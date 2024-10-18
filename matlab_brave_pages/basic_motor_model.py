import numpy as np
import matplotlib.pyplot as plt

# Motor and panel parameters
motor_speed = 5.0  # degrees per second, example motor speed
panel_azimuth = 0.0  # Initial azimuth of the panel (degrees)

# Simulation parameters
time_step = 0.1  # Time step (seconds)
total_time = 10  # Total simulation time (seconds)

# Store data for plotting
times = []
azimuths = []

# Function to simulate motor moving the panel to match the sun's azimuth
def move_panel(sun_azimuth, panel_azimuth, motor_speed, dt):
    error = sun_azimuth - panel_azimuth
    adjustment = np.sign(error) * min(motor_speed * dt, abs(error))
    return panel_azimuth + adjustment

# Simulate the movement over time
for t in np.arange(0, total_time, time_step):
    # Example: Sun's azimuth changes over time
    sun_azimuth = 30 + 2 * t  # Sun's azimuth (degrees), can be dynamically calculated using pysolar

    # Move the panel
    panel_azimuth = move_panel(sun_azimuth, panel_azimuth, motor_speed, time_step)

    # Record for plotting
    times.append(t)
    azimuths.append(panel_azimuth)

    print(f"Time: {t:.1f}s, Panel Azimuth: {panel_azimuth:.2f}, Sun Azimuth: {sun_azimuth:.2f}")

# Plot the result
plt.plot(times, azimuths, label="Panel Azimuth")
plt.xlabel("Time (s)")
plt.ylabel("Panel Azimuth (degrees)")
plt.legend()
plt.show()
