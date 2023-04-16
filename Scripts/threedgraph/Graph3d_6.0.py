import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Your 3D data points here (example data ranges from -1 to 1)
x = np.random.uniform(-1, 1, 10)
y = np.random.uniform(-1, 1, 10)
z = np.random.uniform(-1, 1, 10)

# Scatter plot
ax.scatter(x, y, z)

# Add sensor array
r = 0.5  # radius of the base circle
h = 0.7  # height of the pyramid

# Compute sensor coordinates
sensor_angles = np.array([0, 120, 240]) * np.pi / 180
sensor_x = r * np.cos(sensor_angles)
sensor_y = r * np.sin(sensor_angles)
sensor_z = np.zeros(3)

# Plot sensors
ax.scatter(sensor_x, sensor_y, sensor_z, c='black', marker='o')
ax.scatter(0, 0, h, c='black', marker='o')

# Connect sensors with lines
for xi, yi in zip(sensor_x, sensor_y):
    ax.plot([0, xi], [0, yi], [0, 0], 'k-', lw=1)
    ax.plot([xi, 0], [yi, 0], [0, 0], 'k-', lw=1)
ax.plot([0, 0], [0, 0], [0.7,0], 'k-', lw=1)
##################################################################
    # BEGIN PLOTTING DATA

# Your 3D data points here (example data ranges from -1 to 1)
x = np.random.uniform(-1, 1, 10)
y = np.random.uniform(-1, 1, 10)
z = np.random.uniform(-1, 1, 10)

# Scatter plot
ax.scatter(x, y, z)

# Define colors for each octant
octant_colors = {
    '111': 'red',
    '112': 'green',
    '121': 'blue',
    '122': 'orange',
    '211': 'purple',
    '212': 'cyan',
    '221': 'magenta',
    '222': 'yellow'
}

# Draw lines from the origin to each point and color them according to the octant
for xi, yi, zi in zip(x, y, z):
    octant = f"{1 if xi >= 0 else 2}{1 if yi >= 0 else 2}{1 if zi >= 0 else 2}"
    ax.plot([0, xi], [0, yi], [0, zi], color=octant_colors[octant])

# Set the view to isometric
ax.view_init(elev=45, azim=45)

# Set axis limits
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)

# Create translucent planes for the axes
xx, yy = np.meshgrid(np.linspace(-1, 1, 2), np.linspace(-1, 1, 2))
zz_xy = np.zeros_like(xx)
zz_yz = np.zeros_like(yy)
ax.plot_surface(xx, yy, zz_xy, alpha=0.2, color='red')
ax.plot_surface(zz_yz, xx, yy, alpha=0.2, color='green')
ax.plot_surface(xx, zz_xy, yy, alpha=0.2, color='blue')

# Draw grid lines on the planes
grid_values = np.linspace(-1, 1, 5)

for val in grid_values:
    ax.plot([-1, 1], [val, val], [0, 0], 'k--', lw=0.5)
    ax.plot([val, val], [-1, 1], [0, 0], 'k--', lw=0.5)
    ax.plot([val, val], [0, 0], [-1, 1], 'k--', lw=0.5)
    ax.plot([0, 0], [val, val], [-1, 1], 'k--', lw=0.5)

# Remove old grid lines and display unit labels
ax.xaxis.pane.set_edgecolor('w')
ax.yaxis.pane.set_edgecolor('w')
ax.zaxis.pane.set_edgecolor('w')

ax.set_xticks(grid_values)
ax.set_yticks(grid_values)
ax.set_zticks(grid_values)

ax.grid(False)

plt.show()
