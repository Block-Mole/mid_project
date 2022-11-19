#CREAS LA idea del grafico

import plotly.io as pio
import plotly.graph_objs as go
import plotly_express as px
import matplotlib.pyplot as plt


#creamos grafico de barras con x nombre de paises y datos de la media de goles por partido
def barras(names, goals):
    fig = px.bar(x=names, y=goals, labels={'x':'Paises', "y": "Goles por partido"})
    return fig.show()