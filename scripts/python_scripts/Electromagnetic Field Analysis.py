#Example: Magnetic Field of a Current-Carrying Wire

import numpy as np
import matplotlib.pyplot as plt

# Constants
mu_0 = 4 * np.pi * 1e-7  # Permeability of free space
I = 1  # Current in the wire
print('Permeability of free space: ',mu_0)
print('Current in the wire: ',I)

# Position grid
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

# Magnetic field components
Bx = -mu_0 * I * Y / (2 * np.pi * (X**2 + Y**2))
By = mu_0 * I * X / (2 * np.pi * (X**2 + Y**2))

print(Bx)
print(By)
# Plot the magnetic field
plt.streamplot(X, Y, Bx, By, color=np.sqrt(Bx**2 + By**2), cmap='jet')
plt.title('Magnetic Field of a Current-Carrying Wire')
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar(label='Magnetic Field Strength')
plt.show()


