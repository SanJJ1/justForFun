import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from numpy import sin, cos, tan, sinh, cosh, tanh
a, b, d = 1.32, 1., 0.8
c = a**2 - b**2
u, v = np.mgrid[-4:4:200j, -4:4:200j]
x = u
y = v
z = sin(x) + cos(y)

fig = make_subplots(rows=1, cols=2,
                    specs=[[{'is_3d': True}, {'is_3d': True}]],
                    subplot_titles=['Color corresponds to z', 'Color corresponds to distance to origin'],
                    )

fig.add_trace(go.Surface(x=x, y=y, z=z, colorbar_x=-0.07), 1, 1)
fig.add_trace(go.Surface(x=x, y=y, z=z, surfacecolor=x**2 + y**2 + z**2), 1, 2)
fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                  highlightcolor="limegreen", project_z=True))
fig.update_layout(title_text="Ring cyclide", margin=dict(l=0, r=0, t=30, b=0))

fig.show()