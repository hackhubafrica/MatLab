'''

Question: Determine the transfer function 
𝐻(𝑠) for a system with the following pole-zero configuration: Zeros at 
𝑠=−1 and 𝑠=−2 and poles at 𝑠=−3 and 𝑠=−4
'''
import control as ctrl

# Define the zeros and poles
zeros = [-1, -2]
poles = [-3, -4]

# Construct the transfer function
H = ctrl.TransferFunction(ctrl.zpk2tf(zeros, poles, 1))

# Print the transfer function
print(f"Transfer Function H(s): {H}")

'''
Traceback (most recent call last):
  File "/home/dora/Electrical_ENGINEERING/Sample Question 7: Transfer Function Analysis with Poles and Zeros.py", line 14, in <module>
    H = ctrl.TransferFunction(ctrl.zpk2tf(zeros, poles, 1))
                              ^^^^^^^^^^^
AttributeError: module 'control' has no attribute 'zpk2tf'
[Finished in 4.2s]
'''