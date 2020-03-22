from ipywidgets import VBox, IntSlider
import numpy as np

import plotly
import plotly.graph_objects as go
# import plotly.plotly as py
import plotly.graph_objs as go
#from plotly.widgets import GraphWidget
from IPython.display import display, clear_output, Image
# The old way to use plotly in Jupyter is to use iplot
# either online (if you have an account) or offline
from plotly.offline import iplot


    
x = np.random.randn(8)
y = np.random.randn(8)
# iplot([go.Histogram2dContour(x=x, y=y, contours=dict(coloring='heatmap')),
fig = go.FigureWidget(data=go.Histogram2dContour(x=x, y=y, contours=dict(coloring='heatmap')))
fig.update_layout(
                autosize=True,
                width= 600,
                height=600,
)

islide = IntSlider()

def redo_plot(b):
    print(islide.value)
    
islide.observe(redo_plot)

VBox([islide,fig])