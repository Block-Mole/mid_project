#traemos el grafico y lo juntamos

import streamlit as st
import plotly.graph_objs as go
from data.get_data import goals_favour_per_game, info_paises_all
from data.paint import barras

st.title("Mi projecto")
#hacer un multi select: names = st.multiselect("Selecciona el país", [i["Teams"] for i in pais])

#pais es un alista de dic, con todos los nombres de paises
pais = info_paises_all()
#hacemos una lista con los nombres de los paises
lst_pais = []
for i in pais:
    lst_pais.append(i["Teams"])

#avg_goal_per_game es un alista de dic, con la media de goles por partido de cada pais
avg_goal_per_game = goals_favour_per_game()
#sacamos una lista con esos datos:
goals_avg_game = []
for i in avg_goal_per_game:
    goals_avg_game.append(i["Goals favour per game"])
#ordeno la informacion para
st.plotly_chart(barras(lst_pais, goals_avg_game))
#st.pyplot(graf)