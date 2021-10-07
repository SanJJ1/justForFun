from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
xBounds = (-3, 3)
yBounds = (-3, 3)
x = np.arange(*xBounds, 0.025)
y = np.arange(*yBounds, 0.025)
x, y = np.meshgrid(x, y)
z = (.5 - x**2 + y**2) * np.e**(1 - x**2 - y**2)
# Plot the surface.
surf = ax.plot_surface(x, y, z, cmap ='magma',
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-2, 2)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()