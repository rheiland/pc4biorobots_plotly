#import plotly.graph_objects as go
import plotly.graph_objs as go

import numpy as np

N = 75000
N=1000
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x = np.random.randn(N),
        y = np.random.randn(N),
        mode = 'markers',
        marker = dict(
            line = dict(
                width = 1,
                color = 'DarkSlateGrey')
        )
    )
)

#fig.update_layout(title_text = 'SVG')
fig.update_layout()

fig.show()
