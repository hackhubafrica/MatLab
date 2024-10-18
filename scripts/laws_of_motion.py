import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def sphere_volume(radius):
    """
    Calculate the volume of a sphere given its radius.
    Volume formula: V = (4/3) * π * r^3
    """
    return (4/3) * np.pi * radius**3

def visualize_sphere(radius):
    """
    Visualize the sphere and its volume.
    """
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = radius * np.outer(np.cos(u), np.sin(v))
    y = radius * np.outer(np.sin(u), np.sin(v))
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v))

    fig = plt.figure(figsize=(12, 6))

    # Plotting the 3D surface of the sphere
    ax = fig.add_subplot(121, projection='3d')
    ax.plot_surface(x, y, z, color='b', alpha=0.6)
    ax.set_title(f'Sphere with radius {radius}')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Plotting the volume calculation
    vol = sphere_volume(radius)
    ax2 = fig.add_subplot(122)
    ax2.bar(['Sphere Volume'], [vol], color='b')
    ax2.set_title(f'Volume of Sphere with radius {radius}')
    ax2.set_ylabel('Volume')
    ax2.set_ylim(0, vol * 1.2)  # Set y-axis limit for better visualization

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    radius = float(input("Enter the radius of the sphere: "))
    visualize_sphere(radius)

v=visualize_sphere(radius)
print(v)