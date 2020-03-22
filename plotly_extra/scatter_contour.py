import plotly.graph_objs as go

import numpy as np

N = 75000
N=1000
x = np.random.randn(N)
y = np.random.randn(N)
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x = x,
        y = y,
        mode = 'markers',
        marker = dict(
            line = dict(
                width = 1,
                color = 'DarkSlateGrey')
        )
    )
)
fig.add_trace(
   go.Histogram2dContour(x=x, y=y, contours=dict(coloring='heatmap'))
)

#fig.update_layout(title_text = 'SVG')
fig.update_layout()

fig.show()
