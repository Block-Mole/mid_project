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
def barras2(names, goals):
    fig = px.bar(x=names, y=goals,color=names ,labels={'x':'Pais', "y": "Goles recibidos por partido"})
    return fig

def barras3(names, goals):
    fig = px.bar(x=names, y=goals,color=names ,labels={'x':'Pais', "y": "Goles / Disparos a puerta"})
    return fig


def stages_tree(paises, rondas, df):
    fig = px.treemap(df, path=[px.Constant("all"), 'stage', 'Teams'])
    fig.update_traces(root_color="lightgrey")
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    return fig



def radar_shots_all(stat, name):
    #theta tenemos que obtener los nombres de cada metrica de dispaaro
    theta = []
    values = []
    for i in stat:
        if i != "Teams":
            theta.append(i)
            values.append(stat[i])
    
    radar = go.Scatterpolar(
            r = values, #TENGO QUE METER UNA LISTA CON LOS DATOS NUMERICOS 
            theta = theta, #OTRA LISTA CON LAS KEYS DE ESOS DATOS
            name = name,
            fill = "toself"
        )

    return radar



def radar_shots_tot(stat, name):
    #theta tenemos que obtener los nombres de cada metrica de dispaaro
    theta = []
    values = []
    for i in stat:
        if i != "Teams" and i != "Shots per game" and i != "Shots on target per game" and i != "Shots against per game":
            theta.append(i)
            values.append(stat[i])
    
    radar = go.Scatterpolar(
            r = values, #TENGO QUE METER UNA LISTA CON LOS DATOS NUMERICOS 
            theta = theta, #OTRA LISTA CON LAS KEYS DE ESOS DATOS
            name = name,
            fill = "toself"
        )

    return radar

def radar_shots_per(stat, name):
    #theta tenemos que obtener los nombres de cada metrica de dispaaro
    theta = []
    values = []
    for i in stat:
        if i != "Teams" and i != "Shots total on target" and i != "Shots total" and i != "Shots Total against":
            theta.append(i)
            values.append(stat[i])
    
    radar = go.Scatterpolar(
            r = values, #TENGO QUE METER UNA LISTA CON LOS DATOS NUMERICOS 
            theta = theta, #OTRA LISTA CON LAS KEYS DE ESOS DATOS
            name = name,
            fill = "toself"
        )

    return radar

def tarjetas_per(df):
    fig = px.bar(df, x="teams", y="tarjetas", color="nombre tarjeta", title="Tarjetas amarillas y rojas por partido")
    return fig

def tarjetas_totales(df):
    fig = px.bar(df, x="teams", y="tarjetas", color="nombre tarjeta", title="Tarjetas amarillas y rojas totales")
    return fig