# hace un request a la api
#funcion para traer toda la informacion
import requests
from config.enlace import URL_ST
 #si tiene parametro hay que añadirlo aqui tmnmbn


def goals_favour_per_game():
    return requests.get(URL_ST+f'/info/goals_favour_per_game').json()

def goals_against_per_game():
    return requests.get(URL_ST+f"/info/goals_against_per_game").json()

def info_paises_all():
    return requests.get(URL_ST+f'/info/paises/all').json()

def stage():
    return requests.get(URL_ST+f'/info/stage').json()

def shots_all():
    return requests.get(URL_ST+f'/info/shots/all').json()

def precision_all():
    return requests.get(URL_ST+f'/info/precision/all').json()

def tarjetas_tot():
    return requests.get(URL_ST+f'/info/tarjetas/tot').json()

def tarjetas_avg():
    return requests.get(URL_ST+f'/info/tarjetas/avg').json()


