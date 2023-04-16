import plotly.graph_objs as go
import numpy as np

# Your 3D data here
x = np.random.rand(30)
y = np.random.rand(30)
z = np.random.rand(30)

trace = go.Scatter3d(x=x, y=y, z=z, mode='markers')

data = [trace]

layout = go.Layout(scene=dict(camera=dict(eye=dict(x=1, y=1, z=1))))

fig = go.Figure(data=data, layout=layout)
fig.show()
