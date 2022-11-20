#CREAS LA idea del grafico

import plotly.io as pio
import plotly.graph_objs as go
import plotly_express as px
import matplotlib.pyplot as plt


#creamos grafico de barras con x nombre de paises y datos de la media de goles por partido
def barras(names, goals):
    fig = px.bar(x=names, y=goals,color=names ,labels={'x':'Pais', "y": "Goles por partido"})
    # fig = px.bar(x=names, y=goals,color_continuous_scale=[(0,"blue"), (1,"red")], labels={'x':'Pais', "y": "Goles por partido"})
    #fig.update_traces(marker_color= [(0,"rgb(0,0,255)"), (1,"rgb(255,0,0)")] )
    return fig

    goals_avg_game