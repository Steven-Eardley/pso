from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def randrange(n, vmin, vmax):
    '''
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

n = 100


def animate(i):
    xs = randrange(n, 0, 100)
    ys = randrange(n, 0, 100)
    zs = randrange(n, 0, 100)
    ax.clear()
    ax.scatter(xs, ys, zs, c='r', marker='o')

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
