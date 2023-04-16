import plotly.graph_objs as go
import numpy as np

# Your 3D data points here (example data ranges from -1 to 1)
x = np.random.uniform(-1, 1, 10)
y = np.random.uniform(-1, 1, 10)
z = np.random.uniform(-1, 1, 10)

# Scatter plot
scatter_trace = go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(size=4))

# Draw lines from the origin to each point
lines = []
for xi, yi, zi in zip(x, y, z):
    lines.append(go.Scatter3d(x=[0, xi], y=[0, yi], z=[0, zi], mode='lines', line=dict(color='black')))

# Create translucent planes for the axes
plane_size = 1
opacity = 0.5
planes = [
    go.Surface(x=[[plane_size, plane_size], [-plane_size, -plane_size]], y=[[plane_size, -plane_size], [plane_size, -plane_size]], z=[[0, 0], [0, 0]], opacity=opacity, showscale=False, colorscale=[[0, 'red'], [1, 'red']]),
    go.Surface(x=[[plane_size, plane_size], [-plane_size, -plane_size]], y=[[0, 0], [0, 0]], z=[[plane_size, -plane_size], [plane_size, -plane_size]], opacity=opacity, showscale=False, colorscale=[[0, 'green'], [1, 'green']]),
    go.Surface(x=[[0, 0], [0, 0]], y=[[plane_size, plane_size], [-plane_size, -plane_size]], z=[[plane_size, -plane_size],
