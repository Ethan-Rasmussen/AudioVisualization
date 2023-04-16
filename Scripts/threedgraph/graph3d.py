import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Your 3D data here
x = np.random.rand(30)
y = np.random.rand(30)
z = np.random.rand(30)

ax.scatter(x, y, z)

# Set the view to isometric
ax.view_init(elev=45, azim=45)

plt.show()
