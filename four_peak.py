from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


def f(x, y):
    # local maxima f=1 at (-4,4) and (4,4) but equal global maxima at (0,0) and (0,-4)
    return np.exp(-(x-4)**2 - (y-4)**2) + np.exp(-(x+4)**2 - (y-4)**2) + (2 * np.exp(-x**2 - (y+4)**2)) + (2 * np.exp(-x**2 - y**2))

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-6, 6, 0.25)
Y = np.arange(-6, 6, 0.25)
X, Y = np.meshgrid(X, Y)
Z = f(X, Y)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True)

# Customize the axes.
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_zlim(0, 3)

plt.show()
