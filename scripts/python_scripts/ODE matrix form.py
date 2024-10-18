import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the matrix A and initial condition x0
A = np.array([[3, 2],
              [-1, 4]])

# Initial condition
x0 = np.array([1, 0])  # x1(0) = 1, x2(0) = 0

# Define the ODE function
def ode_system(t, x):
    return A @ x

# Time span for integration
t_span = (0, 5)  # from t=0 to t=5

# Solve the ODE
sol = solve_ivp(ode_system, t_span, x0, dense_output=True)

# Plotting the solutions
t = np.linspace(0, 5, 100)
x1 = sol.sol(t)[0]
x2 = sol.sol(t)[1]

plt.figure(figsize=(10, 6))
plt.plot(t, x1, label='x1(t)')
plt.plot(t, x2, label='x2(t)')
plt.title('Solution of ODE System: x1(t) and x2(t)')
plt.xlabel('Time t')
plt.ylabel('Function value')
plt.legend()
plt.grid(True)
plt.show()