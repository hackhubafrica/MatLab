'''
Sample Question 1: Solving a Differential Equation Using Laplace Transform.py
Question: Solve the differential equation 
𝑑**2𝑦(𝑡)/𝑑𝑡**2+3𝑑𝑦(𝑡)/𝑑𝑡+2𝑦(𝑡)=𝑢(𝑡) with initial conditions 
𝑦(0)=0 and 𝑑𝑦(0)/𝑑𝑡=0 , where 𝑢(𝑡)is a step input.

'''

import sympy as sp

# Define the Laplace variable and time variable
s, t = sp.symbols('s t')
Y = sp.Function('Y')(s)
U = 1 / s  # Laplace transform of the step input u(t)

# Define the differential equation in Laplace domain
diff_eq = s**2 * Y + 3 * s * Y + 2 * Y - U

# Solve for Y(s)
Y_s = sp.solve(diff_eq, Y)[0]

# Perform the inverse Laplace transform to find y(t)
y_t = sp.inverse_laplace_transform(Y_s, s, t)

# Output the result
print(f"Solution y(t): {y_t}")