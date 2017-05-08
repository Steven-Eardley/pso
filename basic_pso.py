""" PSO using numpy arrays for the matrices """

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from functools import reduce, partial
import matplotlib.animation as animation
import numpy as np


def f(v):
    # local maxima f=1 at (-4,4) and (4,4) but equal global maxima at (0,0) and (0,-4)
    [x, y] = v
    return np.exp(-(x-4)**2 - (y-4)**2) + np.exp(-(x+4)**2 - (y-4)**2) + (2 * np.exp(-x**2 - (y+4)**2)) + (2 * np.exp(-x**2 - y**2))

N_PARTICLES = 20
MAX_ITERATIONS = 100
XMIN = YMIN = ZMIN = -6
XMAX = YMAX = ZMAX = 6
ALPHA = 0.6                                                                                      # acceleration constant
BETA = 0.4                                                                                       # acceleration constant
THETA = 0.5                                                                                           # inertia constant

# PSO initialisation
t = 0
converged = False
x = np.zeros((MAX_ITERATIONS, N_PARTICLES, 2))
v = np.zeros((MAX_ITERATIONS, N_PARTICLES, 2))

x[0] = particles = np.random.uniform(XMIN, XMAX, (N_PARTICLES, 2))
x_star = x[0].copy()
g_star = [x[0][np.apply_along_axis(f, 1, x_star).argmax()]]                             # keep a history of global bests

while not converged and t < MAX_ITERATIONS - 1:

    # Velocity update
    alpha_epsilon1 = ALPHA * np.random.rand(N_PARTICLES, 2)
    beta_epsilon2 = BETA * np.random.rand(N_PARTICLES, 2)

    global_update = g_star[-1] - x[t]
    local_update = x_star - x[t]
    v[t+1] = THETA * v[t] + alpha_epsilon1 * global_update + beta_epsilon2 * local_update

    # Position update
    x[t+1] = x[t] + v[t+1]

    # Find new best
    best = np.zeros((N_PARTICLES, 2))
    for i in range(0, N_PARTICLES):
        best[i] = max([x_star[i], x[t+1][i]], key=lambda z: f(z))

    x_star = best
    g_star.append(x_star[np.apply_along_axis(f, 1, x_star).argmax()])

    # Assume convergence if we have same best after 10% of iterations
    ten_percent = int(0.1 * MAX_ITERATIONS)
    if t > ten_percent and reduce(lambda n, m: n and m, map(partial(np.array_equal, g_star[-1]), g_star[-ten_percent:-1])):
        converged = True
    t += 1

print(g_star.pop(), 'after {0} iterations'.format(t))

# Plotting the pso
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# plotting the function
X, Y = np.meshgrid(np.arange(XMIN, XMAX, 0.25), np.arange(YMIN, YMAX, 0.25))
Z = f([X, Y])


def animate(i):
    [xs, ys] = x[i].T
    zs = np.apply_along_axis(f, 1, x[i]).tolist()
    ax.clear()
    ax.set_xlim(XMIN, XMAX)
    ax.set_ylim(YMIN, YMAX)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=True, alpha=0.5)
    ax.scatter(xs, ys, zs, c='k', marker='o')

ani = animation.FuncAnimation(fig, animate, interval=500, frames=t, repeat=False)
plt.show()
