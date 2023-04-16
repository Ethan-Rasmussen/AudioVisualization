import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Your 3D data points here
x = np.random.rand(10)
y = np.random.rand(10)
z = np.random.rand(10)

# Scatter plot
ax.scatter(x, y, z)

# Draw lines from the origin to each point
for xi, yi, zi in zip(x, y, z):
    ax.plot([0, xi], [0, yi], [0, zi], 'k-')

# Set the view to isometric
ax.view_init(elev=45, azim=45)

plt.show()
