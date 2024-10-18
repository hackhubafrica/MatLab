'''
Sample Question 4: Impulse Response of a System.py
Question: Determine the impulse response of a system with transfer function 
𝐻(𝑠)=1/𝑠**2+2𝑠+1
'''
import sympy as sp

# Define the Laplace variable and time variable
s, t = sp.symbols('s t')
H = 1 / (s**2 + 2*s + 1)  # Transfer function

# Impulse response is the inverse Laplace transform of H(s)
h_t = sp.inverse_laplace_transform(H, s, t)

# Output the result
print(f"Impulse Response h(t): {h_t}")