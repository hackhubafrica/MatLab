# Define the differential equation and initial conditions
import scipy as sp
y = sp.Function('y')(t)
eq = sp.Eq(y.diff(t, t) - 2*y.diff(t) - y, 1)
ics = {y.subs(t, 0): -1, y.diff(t).subs(t, 0): 1}

# Compute the Laplace transform
Y = sp.laplace_transform(y, t, s)
Y

'''
# Define the differential equation and initial conditions
y = sp.Function('y')(t)
eq = sp.Eq(y.diff(t, t) - 2*y.diff(t) - y, 1)
ics = {y.subs(t, 0): -1, y.diff(t).subs(t, 0): 1}

# Compute the Laplace transform
Y = sp.laplace_transform(y, t, s)
Y
'''