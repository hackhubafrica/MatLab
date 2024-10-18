# Define the differential equation and initial conditions
y = sp.Function('y')(t)
eq = sp.Eq(y.diff(t, t) - 3*y.diff(t) - 10*y, 1)
ics = {y.subs(t, 0): -1, y.diff(t).subs(t, 0): 2}

# Compute the Laplace transform
Y = sp.laplace_transform(y, t, s)
Y