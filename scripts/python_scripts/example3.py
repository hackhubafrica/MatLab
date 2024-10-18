import sympy as sp

#H(t)=3sinh(2t)+3sin(2t)
# Define variables
t, s = sp.symbols('t s')
# Define the function
h = 3*sp.sinh(2*t) + 3*sp.sin(2*t)

# Compute the Laplace transform
H = sp.laplace_transform(h, t, s)
print('H(s)=',H)


'''
Result:
𝐻(𝑠)=12𝑠/𝑠**2 − 4
'''