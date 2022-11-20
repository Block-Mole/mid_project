# hace un request a la api
#funcion para traer toda la informacion
import requests
from config.enlace import URL_ST
 #si tiene parametro hay que añadirlo aqui tmnmbn


def goals_favour_per_game():
    return requests.get(URL_ST+f'/info/goals_favour_per_game').json()

def info_paises_all():
    return requests.get(URL_ST+f'/info/paises/all').json()

def stage():
    return requests.get(URL_ST+f'/info/stage').json()

#def all_name()

