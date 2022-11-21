#traemos el grafico y lo juntamos

import streamlit as st
import plotly.graph_objs as go
from data.get_data import goals_favour_per_game, info_paises_all,stage, goals_against_per_game, shots_all
from data.paint import barras,barras2,stages_tree,radar_shots_all,radar_shots_tot,radar_shots_per
import pandas as pd
st.title("UEFA EURO 2020 Dashboard")
#hacer un multi select: names = st.multiselect("Selecciona el país", [i["Teams"] for i in pais])

#SIDE BAR CON LAS METRICAS
metricas = ["Elige una métrica","Goles por partido","Goles recibidos por partido", "Rondas de clasificacion","Goles favor/contra por partido", "Estadisticas de disparos"]
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


##Metrica goles en contra por partido
if select_box == "Goles recibidos por partido":
    #avg_goal_per_game es un alista de dic, con la media de goles por partido de cada pais
    avg_goal_per_game = goals_against_per_game()
    #sacamos una lista con esos datos:
    goals_avg_game = []
    for i in avg_goal_per_game:
        goals_avg_game.append(i["Goals against per game"])
    #ordeno la informacion para que se muestre
    df= pd.DataFrame({"teams":lst_pais, "goals": goals_avg_game})
    df.sort_values(by=['goals'], inplace=True, ascending=True)
    lst_pais_asc = [i for i in df["teams"]]
    goals_avg_game_asc = [i for i in df["goals"]]

    st.plotly_chart(barras2(lst_pais_asc, goals_avg_game_asc))
    #creamos el boton para dar la opcion de verlo en grande
    st.write("Haz click para abrir el grafico en una nueva pestaña")
    b0 = st.button("Gráfico")
    if b0 == True:
        barras2(lst_pais_asc,  goals_avg_game_asc).show()

##Metrica goles en a favor/contra por partido

#if select_box == "Goles favor/contra por partido":
    #sacamos una lista con los goles a favor por partido
    #goals_avg_fav = goals_favour_per_game()
    #goals_fav = []
    #for i in goals_avg_fav:
        #goals_fav.append(i["Goals favour per game"])
    #goals_avg_ag = goals_against_per_game()
    #sacamos una lista con los goles en ncontra por partido
    #goals_ag = []
    #for i in goals_avg_ag:
        #goals_ag.append(i["Goals against per game"])
    #juntamos los datos
    #st.plotly_chart(stack_bars(goals_fav,goals_ag))




#METRICA DE RONDAS
#HACER UN MULTY SELECT
if select_box == "Rondas de clasificacion":
    #crear un df con los paises y sus rondas
    stage_tot = stage()
    lst_stage_tot = []
    for i in stage_tot:
        lst_stage_tot.append(i["Stage"])
    
    df= pd.DataFrame({"teams":lst_pais, "stage": lst_stage_tot })

    #creamos el cuadro con todos
    st.write(f"Cuadro con las fases de clasificación y los equipos que quedaron eliminados en cada una")
    st.plotly_chart(stages_tree(df["teams"], df["stage"], df))

    #creamos la barra
    stages_lst = ["Final","Semi-finals","Quarter-finals","Round of 16", "Group stage: Matchday 3"]
    stages = st.select_slider("Selecciona la/s ronda/s para ver los equipos que cayeron elimindados en cada una", options = stages_lst[::-1])


    if stages != "Final":
        st.write(f"Los equipos eliminados en la ronda **{stages}** fueron:")
    else:
        st.write(f"Los paises que llegaron a la **{stages}** fueron:")
    
    #filtrado para que salgan los paieses en funcion de la stage seleccionada
    st.dataframe(df["teams"][df["stage"]==stages])

    if stages == "Final":
        st.write(f"Siendo el pais vencedor: ***Italy***")
    
    

##METRICA RADAR DE DISPAROS
if select_box == "Estadisticas de disparos":
    st.header("Gráficos de las estdísticas de disparos")
    st.write("\n")
    disparos = shots_all()
    elegidos = st.multiselect("Seleccione los paieses que desee comparar", [i["Teams"] for i in pais])
    
    stats = []
    for name in elegidos:
        for j in disparos:
            if j["Teams"] == name:
                stats.append((name, j))

    if stats:
        st.subheader("Grafico con todos los datos de disparos")
        graph0 = go.Figure()
        for name,stat in stats:
            graph0.add_trace(radar_shots_all(stat, name))

        st.plotly_chart(graph0)

        #creamos el boton para dar la opcion de verlo en grande
        st.write("Haz click para abrir el grafico en una nueva pestaña")
        b0 = st.button("Gráfico de all shot data")
        if b0 == True:
            graph0.show()
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")


    #creamos el radar para los pergame
    if stats:
        st.subheader("Grafico con solo los datos por partido")
        graph1 = go.Figure()
        for name,stat in stats:
            graph1.add_trace(radar_shots_per(stat, name))

        st.plotly_chart(graph1)
            
        #creamos el boton para dar la opcion de verlo en grande
        st.write("Haz click para abrir el grafico en una nueva pestaña")
        b1 = st.button("Gráfico de por partido")
        if b1 == True:
            graph1.show()
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")

    #creamos el radar para los tot
    if stats:
        st.subheader("Grafico con solo los datos totales")
        graph2 = go.Figure()
        for name,stat in stats:
            graph2.add_trace(radar_shots_tot(stat, name))

        st.plotly_chart(graph2)
        
        #creamos el boton para dar la opcion de verlo en grande
        st.write("Haz click para abrir el grafico en una nueva pestaña")
        b2 = st.button("Gráfico de total")
        if b2 == True:
            graph2.show()



