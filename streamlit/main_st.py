#traemos el grafico y lo juntamos

import streamlit as st
import plotly.graph_objs as go
from data.get_data import goal_per_game, info_paises_all
from data.paint import goals_favour_per_game

st.title("Mi projecto")


pais = info_paises_all()

name = st.multiselect("Selecciona el país", [i["Teams"] for i in pais])

goals = []
for i in name: #name es una lista de lo seleccionado en multi, y esta request solo admite str
    goals.append(goal_per_game(i))
     
graf = goals_favour_per_game(name, goals) 

st.pyplot(graf)