#CREAS LA idea del grafico

import matplotlib.pyplot as plt

#name viene de streamlit, del multyselect
#goals viene de main de la api

def goals_favour_per_game(name, goals): #stats es una lista con dic
    goal = []
    for i in goals:
        for j in i:
            goal.append(j["Goals favour per game"])
    return plt.bar(name, goal)