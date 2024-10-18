import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
import sympy as sp
# Define the transfer function H(s)
numerator = [1]
denominator = [1, 2 ,1]
H = ctrl.TransferFunction(numerator, denominator)

print(type(H))


t, s = sp.symbols('t s')

H = (1)/(s**2 + 2*s + 1)

h = sp.inverse_laplace_transform(H,s,t)
print(h)


