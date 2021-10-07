from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
xBounds = (-3, 3)
yBounds = (-3, 3)
zBounds = (-5, 5)
x = np.arange(*xBounds, .01)
y = np.arange(*yBounds, .01)
x, y = np.meshgrid(x, y)


def f(x, y):
    return x * y
    # return (.5 - x**2 + y**2) * np.e**(1 - x**2 - y**2)
    # return (.5 * x ** 4) - (2 * x ** 3) + (4 * x * y) + (y ** 2)
    # return (2 * x**3) + (x * y**2) + (5 * x**2) + (y**2)


z = f(x, y)
# Plot the surface.
surf = ax.plot_surface(x, y, z, cmap='magma',
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(*zBounds)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

ax.set_xlabel('$X$')
ax.set_ylabel('$Y$')
ax.set_zlabel('Z')
# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=.4, aspect=5)

plt.show()

print(f(4, -8))