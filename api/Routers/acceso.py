from fastapi import APIRouter
from Database.mongodb import db #estamos entrando en la carpeta Database, el file mongodb, y de ahi obteniendo la variable db
from bson import json_util #transformar json porque al hacer la llamada nos da un bson mo un json. Json util nos pasa la lista a str
from json import loads #cargar en json

router = APIRouter()


@router.get("/info/paises/all") #nos devuelve una lista con dic con los nombres de todos los paises
def names():
    q = list(db["paises"].find({},{"_id":0, "Teams":1}))
    return loads(json_util.dumps(q))

@router.get("/info/goals_favour_per_game") #nos todos los goles por partido de cada pais(todos)
def goals_per_game():
    q = list(db["paises"].find({},{"_id":0, "Goals favour per game":1}))
    return loads(json_util.dumps(q))

@router.get("/info/goals_against_per_game") #nos todos los goles recibirdos por partido de cada pais(todos)
def goals_against_per_game():
    q = list(db["paises"].find({},{"_id":0, "Goals against per game":1}))
    return loads(json_util.dumps(q))


@router.get("/info/stage") #devuelve la ronda en la que ha quedado eliminada cada pais
def stage():
    q = list(db["paises"].find({},{"_id":0, "Stage":1}))
    return loads(json_util.dumps(q))

@router.get("/info/shots/all") #devuelve toda la info de los disparos
def shots_all():
    q = list(db["paises"].find({},{"_id":0,"Teams":1, "Shots total":1, "Shots total on target":1, "Shots per game":1, "Shots on target per game":1, "Shots Total against":1, "Shots against per game":1}))
    return loads(json_util.dumps(q))

@router.get("/info/precision/all") #devuelve toda la info de los disparos
def precision_all():
    q = list(db["paises"].find({},{"_id":0,"Accuracy":1}))
    return loads(json_util.dumps(q))

@router.get("/info/tarjetas/tot") #devuelve toda la info de los disparos
def tarjetas_tot():
    q = list(db["paises"].find({},{"_id":0,"Yellow cards total":1, "Red cards total":1}))
    return loads(json_util.dumps(q))

@router.get("/info/tarjetas/avg") #devuelve toda la info de los disparos
def tarjetas_avg():
    q = list(db["paises"].find({},{"_id":0,"Yellow cards per game":1, "Red cards per game":1}))
    return loads(json_util.dumps(q))




#@router.get("/equipo/goles") #sumar todos los valores dentro de un filtro
#def todos_goles_avg():
    #res = db["paises"].aggregate([{"$group": {"_id": "$Team", "goles_favor":{"$sum":"$Goals favour per game"}}}])
    #return loads(json_util.dumps(res))



#@router.get("/paises") #en la ruta hay que escribir /paises?pais=Spain
#def nombre(pais:str):
    #q = db["paises_2"].find({"Teams": pais},{"_id":0})
    #return loads(json_util.dumps(q))

