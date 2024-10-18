#F(s)= 1/(s+1)(s 2−1)

# Define the Laplace transform
F = 1 / ((s+1) * (s**2 - 1))

# Compute the inverse Laplace transform
f = sp.inverse_laplace_transform(F, s, t)
f


'''
# Define the Laplace transform
F = 1 / ((s+1) * (s**2 - 1))

# Compute the inverse Laplace transform
f = sp.inverse_laplace_transform(F, s, t)
f
'''