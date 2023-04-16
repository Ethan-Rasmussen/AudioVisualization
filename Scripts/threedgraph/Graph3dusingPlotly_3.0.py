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

data = [scatter_trace] + lines

layout = go.Layout(scene=dict(xaxis=dict(range=[-1, 1]), yaxis=dict(range=[-1, 1]), zaxis=dict(range=[-1, 1]), camera=dict(eye=dict(x=1, y=1, z=1))))

fig = go.Figure(data=data, layout=layout)
fig.show()
