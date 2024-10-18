import numpy as np
import matplotlib.pyplot as plt

# Time step size and total time
dt = 0.01  # time step
t_total = 10  # total time in seconds
time_steps = int(t_total / dt)

# Initialize arrays to store the results
time = np.linspace(0, t_total, time_steps)
y = np.zeros(time_steps)   # position
yd = np.zeros(time_steps)  # velocity
ydd = np.zeros(time_steps)  # acceleration
u = np.zeros(time_steps)   # input

# Set initial conditions
y[0] = 2     # initial position
yd[0] = 4    # initial velocity
u[0] = 6     # initial input

# System dynamics function for second-order system
def system_dynamics(y, yd, u):
    return u - y - yd  # Example dynamics (can be modified)

# Time stepping loop using Euler integration
for n in range(time_steps - 1):
    # Compute acceleration at time t_n
    ydd[n] = system_dynamics(y[n], yd[n], u[n])
    
    # Euler method to update velocity and position
    yd[n + 1] = yd[n] + ydd[n] * dt
    y[n + 1] = y[n] + yd[n] * dt

# Plot the results
plt.plot(time, y, label='Position (y)')
plt.plot(time, yd, label='Velocity (yd)')
plt.plot(time, ydd, label='Acceleration (ydd)')
plt.xlabel('Time (s)')
plt.ylabel('Magnitude')
plt.legend()
plt.grid(True)
plt.title('Numerical Solution with Initial Conditions')
plt.show()
