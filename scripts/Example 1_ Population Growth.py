import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the differential equation function
def population_growth(P, t):
    k = np.log(2) / 10  # Growth rate constant
    dPdt = k * P
    return dPdt

# Initial population
P0 = 40  # million

# Time points to solve for
t = np.linspace(0, 20, 100)

# Solve the differential equation
P = odeint(population_growth, P0, t)

# Plot the results
plt.figure(figsize=(8, 6))
plt.plot(t, P, label='Population growth')
plt.title('Population Growth Over Time')
plt.xlabel('Time (years)')
plt.ylabel('Population (millions)')
plt.grid(True)
plt.legend()
plt.show()

# Population at t = 20 years
P_20 = float(P[-1])
print(f"Population at t = 20 years: {P_20:.2f} million")


'''
Explanation:

Step 1: Define the differential equation function population_growth which represents exponential population growth.
Step 2: Set initial conditions (P0) and time points (t) for which to solve the equation.
Step 3: Use odeint from scipy.integrate to solve the differential equation numerically.
Step 4: Plot the results to visualize how population grows over time.
Step 5: Print the population at a specific time (t = 20) to see the final population size.

'''