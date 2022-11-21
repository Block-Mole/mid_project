
from numpy import random
import streamlit as st
import plotly.graph_objs as go
from data.get_data import goals_favour_per_game, info_paises_all,stage, goals_against_per_game, shots_all,precision_all,tarjetas_avg,tarjetas_tot
from data.paint import barras,barras2,barras3,stages_tree,radar_shots_all,radar_shots_tot,radar_shots_per,tarjetas_per, tarjetas_totales
import pandas as pd



st.title("UEFA EURO 2020 Dashboard")

#SIDE BAR CON LAS METRICAS
metricas = ["Home","Datos de goles", "Datos de rondas de clasificacion", "Datos de estadisticas de disparos", "Datos de tarjetas"]
st.sidebar.title("Menu")
select_box = st.sidebar.selectbox("Seleccione la metrica que desee ver",options = metricas)


if select_box == "Home":

    st.header("¡Bienvenido!" )
    st.write("Utiliza el navegador a la izquierda que se muestra en el sidebar, para acceder a las diferentes metricas del torneo")

    g = ["https://media2.giphy.com/media/U2S3BeydJ3ygflT5Gw/giphy.gif", 
    "https://media4.giphy.com/media/LNxb8Iq8BPFrNC6HfU/giphy.gif", 
    "https://media1.giphy.com/media/3o72F0RQC4xHzSrWMg/giphy.gif", 
    "https://media1.giphy.com/media/NYe8u6VliRJjV8cHgi/giphy.gif", 
    "https://media3.giphy.com/media/4eEs61XaMvUPVWh6bc/giphy.gif"]
   
    gif = g[random.randint(5)]
    _left, mid, _right = st.columns(3)
    with _left:
        st.image(gif, width=800)

#creo una lista de paises que puede ser de utilidad para varias metricas
#pais es un alista de dic, con todos los nombres de paises
pais = info_paises_all()
lst_pais = []
for i in pais:
    lst_pais.append(i["Teams"])


#METRICAS DE GOLES


if select_box == "Datos de goles":
    
    #METRICA DE GOLES A FAVOR POR PARTIDO
    st.header("Goles a favor por partido")
    st.write("Los goles que marca cada pais por partido.")
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
    pdf = barras(lst_pais_desc, goals_avg_game_desc)
    col1, col2 = st.columns(2)
    with col1:
        st.write("Haz click para abrir el grafico en una nueva pestaña")
        b0 = st.button("Gráfico 1")
        if b0 == True:
            barras(lst_pais_desc,  goals_avg_game_desc).show()
    #with col2:
        #st.write("Haz click para descargar el grafico en pdf")

        #fn = 'scatter.png'
        #img = io.BytesIO()
        #plt.savefig(img, format='png')
        
        #btn = st.download_button(
            #label="Download image",
            #data=img,
            #file_name=fn,
            #mime="image/png")

    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")


    ##METRICA GOLES EN CONTRA POR PARTIDO
    st.header("Goles en contra por partido")
    st.write("Los goles que recibe cada pais por partido.")
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
    b1 = st.button("Gráfico 2")
    if b1 == True:
        barras2(lst_pais_asc,  goals_avg_game_asc).show()
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")


    #METRICA DE LA ACCURACY
    st.header("Precisión")
    st.write("La precision es: del total de los disparos a puerta, cuantos acaban siendo gol. Es decir, de cada disparo a puerta cuantas probabilidades tiene de acabar en gol.")
    team_accuracy = precision_all()
    precision = []
    for i in team_accuracy:
        precision.append(i["Accuracy"])
    st.plotly_chart(barras3(lst_pais, precision))
    #creamos el boton para dar la opcion de verlo en grande
    st.write("Haz click para abrir el grafico en una nueva pestaña")
    b3 = st.button("Gráfico 3")
    if b3 == True:
        barras3(lst_pais, precision).show()



#METRICA DE RONDAS
#HACER UN MULTY SELECT
if select_box == "Datos de rondas de clasificacion":
    #crear un df con los paises y sus rondas
    stage_tot = stage()
    lst_stage_tot = []
    for i in stage_tot:
        lst_stage_tot.append(i["Stage"])
    
    df= pd.DataFrame({"Teams":lst_pais, "stage": lst_stage_tot })

    #creamos el cuadro con todos
    st.header("Rondas de clasificacion")
    st.write(f"Cuadro con las fases de clasificación y los equipos que quedaron eliminados en cada una")
    st.plotly_chart(stages_tree(df["Teams"], df["stage"], df))
    b0 = st.button("Abrir en otra pestaña")
    if b0 == True:
        stages_tree(df["Teams"], df["stage"], df).show()

    #creamos la barra
    stages_lst = ["Final","Semi-finals","Quarter-finals","Round of 16", "Group stage: Matchday 3"]
    stages = st.select_slider("Selecciona la/s ronda/s para ver los equipos que cayeron elimindados en cada una", options = stages_lst[::-1])


    if stages != "Final":
        st.write(f"Los equipos eliminados en la ronda **{stages}** fueron:")
    else:
        st.write(f"Los paises que llegaron a la **{stages}** fueron:")
    
    #filtrado para que salgan los paieses en funcion de la stage seleccionada
    st.dataframe(df["Teams"][df["stage"]==stages])

    if stages == "Final":
        st.write(f"Siendo el pais vencedor: ***Italy***")
    
    



##METRICA RADAR DE DISPAROS
if select_box == "Datos de estadisticas de disparos":
    st.header("Gráficos de las estdísticas de disparos")
    st.write("A continuacion, puedes seleccionar los paises que deseas comparar los datos de los disparos en un grafico de radar o *'araña'*")
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
        st.write("En este grafico, puedes ver una comparativa de todos los datos sobre los disparos de cada pais")
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
        st.write("En este grafico, puedes ver una comparativa de los datos de los disparos por partido de cada pais")
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
        st.write("En este grafico, puedes ver una comparativa de los datos de los disparos totales de cada pais")
        graph2 = go.Figure()
        for name,stat in stats:
            graph2.add_trace(radar_shots_tot(stat, name))

        st.plotly_chart(graph2)
        
        #creamos el boton para dar la opcion de verlo en grande
        st.write("Haz click para abrir el grafico en una nueva pestaña")
        b2 = st.button("Gráfico de total")
        if b2 == True:
            graph2.show()



#METRICA DE TARJETAS

if select_box == "Datos de tarjetas":
    #DATA DE TARJETAS POR PARTIDO
    st.header("Gráficos de las estdísticas de tarjetas por partido")
    st.write("En el siguiente gráfico, podra ver las tarjetas amarillas y rojas por partido que ha recibido cada pais. Nota: las segundas tarjetas amarillas se han contabilizado como una roja")
    st.write("\n")

    tarjetas_yellow = []
    tarjetas_red = []
    for i in tarjetas_avg():
        tarjetas_yellow.append(i["Yellow cards per game"])
        tarjetas_red.append(i["Red cards per game"])
    df1 = pd.DataFrame({"teams":lst_pais,"nombre tarjeta": "yellow" ,"tarjetas": tarjetas_yellow})
    df2 = pd.DataFrame({"teams":lst_pais, "nombre tarjeta": "red","tarjetas": tarjetas_red})
    df3 = pd.concat([df1,df2], ignore_index=True)
    st.plotly_chart(tarjetas_per(df3))

    #creamos el boton para dar la opcion de verlo en grande
    st.write("Haz click para abrir el grafico en una nueva pestaña")
    b0 = st.button("Gráfico 1")
    if b0 == True:
        tarjetas_per(df3).show()

    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")

    #DATA DE TARJETAS TOTALES
    st.header("Gráficos de las estdísticas de tarjetas totales")
    st.write("En el siguiente gráfico, podra ver las tarjetas amarillas y rojas totales en el torneo que ha recibido cada pais. Nota: las segundas tarjetas amarillas se han contabilizado como una roja")
    st.write("\n")

    tarjetas_yellow = []
    tarjetas_red = []
    for i in tarjetas_tot():
        tarjetas_yellow.append(i["Yellow cards total"])
        tarjetas_red.append(i["Red cards total"])
    df1 = pd.DataFrame({"teams":lst_pais,"nombre tarjeta": "yellow" ,"tarjetas": tarjetas_yellow})
    df2 = pd.DataFrame({"teams":lst_pais, "nombre tarjeta": "red","tarjetas": tarjetas_red})
    df3 = pd.concat([df1,df2], ignore_index=True)
    st.plotly_chart(tarjetas_totales(df3))

    #creamos el boton para dar la opcion de verlo en grande
    st.write("Haz click para abrir el grafico en una nueva pestaña")
    b1 = st.button("Gráfico 2")
    if b1 == True:
        tarjetas_totales(df3).show()




