# hace un request a la api
#funcion para traer toda la informacion
import requests
from config.enlace import URL_ST
 #si tiene parametro hay que añadirlo aqui tmnmbn


def stage(ronda):
    return requests.get(URL_ST+f'/info/stage/{ronda}').json() # f pra que tome el parametro , tomando info de la api

def info_all(pais):
    return requests.get(URL_ST+f'/info/all/{pais}').json()

def goal_per_game(pais):
    return requests.get(URL_ST+f'/info/goals_favour_per_game').json()

def info_paises_all():
    return requests.get(URL_ST+f'/info/paises/all').json()

#def all_name()

