'''
A transfer function in control theory represents the 
relationship between the input and output of a linear 
time-invariant system in the frequency domain. 
It is typically represented as the ratio of the Laplace 
transform of the output to the Laplace transform of the 
input under zero initial conditions.
'''
import numpy as np
import control as ctrl

# Define system parameters
numerator = [1]
denominator = [1, 2, 1]  # Example denominator coefficients

# Create transfer function
sys_tf = ctrl.TransferFunction(numerator, denominator)

# Print transfer function
print(f"Transfer Function: ")
print(sys_tf)


'''
Explanation:
control.TransferFunction from the control library creates a transfer function object sys_tf.

In this example, the transfer function is 
1/𝑠**2+2𝑠+1,represented by the numerator [1] and denominator [1, 2, 1] coefficients.
'''