import sympy as sp

x = sp.symbols('x')
f = (2*x)**2

# Differentiation
df_dx = sp.diff(f, x)
print(f"Derivative: {df_dx}")

# Integration
integral_f = sp.integrate(f, x)
print(f"Integral: {integral_f}")
