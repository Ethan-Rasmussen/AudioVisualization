import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Your 3D data points here (example data ranges from -1 to 1)
x = np.random.uniform(-1, 1, 30)
y = np.random.uniform(-1, 1, 30)
z = np.random.uniform(-1, 1, 30)

# Scatter plot
ax.scatter(x, y, z)

# Add sensor array
r = 0.5  # radius of the base circle
h = 0.7  # height of the pyramid
thickness = 0.06  # thickness of the array arms

# Compute sensor coordinates
sensor_angles = np.array([0, 120, 240]) * np.pi / 180
sensor_x = r * np.cos(sensor_angles)
sensor_y = r * np.sin(sensor_angles)
sensor_z = np.zeros(3)

# Plot sensors
#ax.scatter(sensor_x, sensor_y, sensor_z, c='black', marker='o')
#ax.scatter(0, 0, h, c='black', marker='o')

def cylinder_between_points(x1, y1, z1, x2, y2, z2, thickness, resolution=20):
    v = np.array([x2 - x1, y2 - y1, z2 - z1])
    mag = np.linalg.norm(v)
    v = v / mag

    not_v = np.array([1, 1, 0])
    if (v == not_v).all():
        not_v = np.array([1, 0, 0])

    n1 = np.cross(v, not_v)
    n1 /= np.linalg.norm(n1)
    n2 = np.cross(v, n1)

    t = np.linspace(0, mag, resolution)
    theta = np.linspace(0, 2 * np.pi, resolution)
    t_grid, theta_grid = np.meshgrid(t, theta)

    X = x1 + thickness * (n1[0] * np.cos(theta_grid) + n2[0] * np.sin(theta_grid)) + v[0] * t_grid
    Y = y1 + thickness * (n1[1] * np.cos(theta_grid) + n2[1] * np.sin(theta_grid)) + v[1] * t_grid
    Z = z1 + thickness * (n1[2] * np.cos(theta_grid) + n2[2] * np.sin(theta_grid)) + v[2] * t_grid

    return X, Y, Z

# Connect sensors with lines (cylinders)
for xi, yi in zip(sensor_x, sensor_y):
    X, Y, Z = cylinder_between_points(0, 0, -.2, xi, yi, -.2, thickness)
    ax.plot_surface(X, Y, Z, color='black')

X, Y, Z = cylinder_between_points(0, 0, -.2, 0, 0, h-.2, thickness)
ax.plot_surface(X, Y, Z, color='black')

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

#Draw lines from the origin to each point and color them according to the octant
for xi, yi, zi in zip(x, y, z):
    octant = f"{1 if xi >= 0 else 2}{1 if yi >= 0 else 2}{1 if zi >= 0 else 2}"
    ax.plot([0, xi], [0, yi], [0, zi], color=octant_colors[octant])

#Set the view to isometric
ax.view_init(elev=45, azim=45)

#Set axis limits
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)

#Create translucent planes for the axes
xx, yy = np.meshgrid(np.linspace(-1, 1, 2), np.linspace(-1, 1, 2))
zz_xy = np.zeros_like(xx)
zz_yz = np.zeros_like(yy)
ax.plot_surface(xx, yy, zz_xy, alpha=0.15, color='red')
ax.plot_surface(zz_yz, xx, yy, alpha=0.15, color='green')
ax.plot_surface(xx, zz_xy, yy, alpha=0.15, color='blue')

#Draw grid lines on the planes
grid_values = np.linspace(-1, 1, 5)

for val in grid_values:
    ax.plot([-1, 1], [val, val], [0, 0], 'k--', lw=0.5)
    ax.plot([val, val], [-1, 1], [0, 0], 'k--', lw=0.5)
    ax.plot([val, val], [0, 0], [-1, 1], 'k--', lw=0.5)
    ax.plot([0, 0], [val, val], [-1, 1], 'k--', lw=0.5)

#Remove old grid lines and display unit labels
ax.xaxis.pane.set_edgecolor('g')
ax.yaxis.pane.set_edgecolor('r')
ax.zaxis.pane.set_edgecolor('b')

ax.set_xticks(grid_values)
ax.set_yticks(grid_values)
ax.set_zticks(grid_values)

ax.grid(False)


# Generate a sphere
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = 0.15 * np.cos(u) * np.sin(v)
y = 0.15 * np.sin(u) * np.sin(v)
z = 0.02* np.cos(v)

# Plot the sphere in red
ax.plot_surface(x, y, z, color='red')

plt.show()
