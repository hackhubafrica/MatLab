import matplotlib.pyplot as plt
# import control as ctrl

# Define the transfer function H(s) = 1 / (s^2 + 2s + 1)
num = [1,5]  # Numerator
den = [1, 2, 1]  # Denominator

H = ctrl.TransferFunction(num, den)

# Plot the poles and zeros
plt.figure(figsize=(6, 6))
ctrl.pzmap(H, plot=True, grid=True)
plt.title('Pole-Zero Plot')
plt.xlabel('Real')
plt.ylabel('Imaginary')

# Show the plot
plt.show()
