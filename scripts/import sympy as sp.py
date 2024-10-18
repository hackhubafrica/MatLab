import sympy as sp

x = sp.symbols('x')
f = (2*x)**2

# Differentiation
df_dx = sp.diff(f, x)
print(f"Derivative: {df_dx}")

# Integration
integral_f = sp.integrate(f, x)
print(f"Integral: {integral_f}")


# Define symbolic variables
s, t = sp.symbols('s t')
m, b, k = 1, 2, 1  # Example values for mass, damping, and spring constant

# Define Laplace transform of the system
F_s = 1  # Assuming unit impulse force for simplicity
X_s = F_s / (m * s**2 + b * s + k)

# Perform inverse Laplace transform to get time-domain solution
x_t = sp.inverse_laplace_transform(X_s, s, t)

# Display the result
print("Time-domain solution x(t):", x_t)

