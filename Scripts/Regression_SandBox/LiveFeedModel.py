from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from TestRegressedListener import converted_sound_coord


# Create figure
fig = plt.figure(figsize=(15, 15))
ax = plt.axes(projection='3d')

# Set axes limits
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

# Set axes labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Add sensor array
r = 0.5  # radius of the base circle
h = 0.7  # height of the pyramid
thickness = 0.06  # thickness of the array arms

# Compute sensor coordinates
sensor_angles = np.array([0, 120, 240]) * np.pi / 180
sensor_x = r * np.cos(sensor_angles)
sensor_y = r * np.sin(sensor_angles)
sensor_z = np.zeros(3)


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

X, Y, Z = cylinder_between_points(0, 0, -.2, 0, 0, h - .2, thickness)
ax.plot_surface(X, Y, Z, color='black')

# Initialize data
data = np.array([[0, 0, 0]])

# Initialize scatter plot
scatter = ax.scatter(data[:, 0], data[:, 1], data[:, 2], c='r', marker='o')


def update(x, y, z):
    # Function to update scatter plot
    print(x)
    print(y)
    print(z)
    data = np.column_stack((x,y,z))
    scatter._offsets3d = x, y, z
    return scatter,

print(converted_sound_coord)
print(converted_sound_coord[0])
print(converted_sound_coord[1])
print(converted_sound_coord[2])

ax.scatter(converted_sound_coord[0], converted_sound_coord[1], converted_sound_coord[2], c='r', marker='o')




#update(converted_sound_coord)


# Define animation
ani = animation.FuncAnimation(fig, update, frames=[], interval=100)

# Show plot
plt.show()
