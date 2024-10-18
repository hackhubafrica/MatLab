'''
Sample Question 6: Second-Order Differential Equation.py
Question: Solve the differential equation 
𝑑**2𝑦(𝑡)/𝑑𝑡**2+4𝑑𝑦(𝑡)𝑑𝑡+4𝑦(𝑡)=𝑒−3𝑡 with 

initial conditions 𝑦(0)=0 and 𝑑𝑦(0)/𝑑𝑡=0
'''

import sympy as sp

# Define the Laplace variable and time variable
s, t = sp.symbols('s t')
Y = sp.Function('Y')(s)
U = sp.exp(-3*t) / s  # Laplace transform of the input e^(-3t)

# Define the differential equation in Laplace domain
diff_eq = s**2 * Y + 4 * s * Y + 4 * Y - U

# Solve for Y(s)
Y_s = sp.solve(diff_eq, Y)[0]

# Perform the inverse Laplace transform to find y(t)
y_t = sp.inverse_laplace_transform(Y_s, s, t)

# Output the result
print(f"Solution y(t): {y_t}")