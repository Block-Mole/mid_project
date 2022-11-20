#traemos el grafico y lo juntamos

import streamlit as st
import plotly.graph_objs as go
from data.get_data import goals_favour_per_game, info_paises_all,stage
from data.paint import barras
import pandas as pd
st.title("UEFA EURO 2020 Dashboard")
#hacer un multi select: names = st.multiselect("Selecciona el país", [i["Teams"] for i in pais])

#SIDE BAR CON LAS METRICAS
metricas = ["Elige una métrica","Goles por partido", "Rondas de clasificacion"]
select_box = st.sidebar.selectbox("Elige una metrica para mostrar",options = metricas)

#creo una lista de paises que puede ser de utilidad para varias metricas
#pais es un alista de dic, con todos los nombres de paises
pais = info_paises_all()
lst_pais = []
for i in pais:
    lst_pais.append(i["Teams"])


#METRICA GOLES POR PARTIDO

if select_box == "Goles por partido":
    #avg_goal_per_game es un alista de dic, con la media de goles por partido de cada pais
    avg_goal_per_game = goals_favour_per_game()
    #sacamos una lista con esos datos:
    goals_avg_game = []
    for i in avg_goal_per_game:
        goals_avg_game.append(i["Goals favour per game"])
        #ordeno la informacion para que se muestre
    df= pd.DataFrame({"teams":lst_pais, "goals": goals_avg_game})
    df.sort_values(by=['goals'], inplace=True, ascending=False)
    lst_pais_desc = [i for i in df["teams"]]
    goals_avg_game_desc = [i for i in df["goals"]]

    st.plotly_chart(barras(lst_pais_desc, goals_avg_game_desc))
    #creamos el boton para dar la opcion de verlo en grande
    st.write("Haz click para abrir el grafico en una nueva pestaña")
    b0 = st.button("Gráfico")
    if b0 == True:
        barras(lst_pais_desc,  goals_avg_game_desc).show()

#METRICA DE RONDAS
#HACER UN MULTY SELECT
if select_box == "Rondas de clasificacion":
    stages_lst = ["Final","Semi-finals","Quarter-finals","Round of 16", "Group stage: Matchday 3"]
    stages = st.select_slider("Selecciona la/s ronda/s para ver los equipos que cayeron elimindados en cada una", stages_lst[::-1])
    
    stage_tot = stage()
    lst_stage_tot = []
    for i in stage_tot:
        lst_stage_tot.append(i["Stage"])
    df= pd.DataFrame({"teams":lst_pais, "stage": lst_stage_tot })
    if stages != "Final":
        st.write(f"Los equipos eliminados en la ronda **{stages}** fueron:")
    else:
        st.write(f"Los paises que llegaron a la **{stages}** fueron:")
    
    st.dataframe(df["teams"][df["stage"]==stages])

    if stages == "Final":
        st.write(f"Siendo el pais vencedor: ***Italy***")