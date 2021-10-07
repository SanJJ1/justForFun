import numpy as np
import plotly.graph_objects as go

my_data = np.random.rand(65,3)  # toy 3D points
marker_data = go.Mesh3d(
    x=my_data[:,0],
    y=my_data[:,1],
    z=my_data[:,2],
    # marker=go.scatter3d.Marker(size=3),
    opacity=0.8,
    # mode='markers'
)
fig=go.Figure(data=marker_data)
fig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0)
)
fig.show()