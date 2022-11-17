from fastapi import APIRouter
from Database.mongodb import db #estamos entrando en la carpeta Database, el file mongodb, y de ahi obteniendo la variable db
from bson import json_util #transformar json porque al hacer la llamada nos da un bson mo un json. Json util nos pasa la lista a str
from json import loads #cargar en json

router = APIRouter()

@router.get("/info/all/{pais}") #nos devuelve toda la informacion de un pais
def allinfo(pais:str):
    q = db["paises"].find({"Teams": pais.capitalize()},{"_id":0}) 
    return loads(json_util.dumps(q)) #esto es porque q nos devuelve una lista y lo queremos en json

@router.get("/info/name/{pais}") #nos devuelve el nombre del pais
def name(pais:str):
    q = list(db["paises"].find({"Teams": pais.capitalize()},{"_id":0, "Teams":1}))
    return loads(json_util.dumps(q))

@router.get("/info/paises/all") #nos devuelve todos los nombres de los paises
def names():
    q = list(db["paises"].find({},{"_id":0, "Teams":1}))
    return loads(json_util.dumps(q))

@router.get("/info/stage/{ronda}") #nos devuelve segun la ronda los paises eliminados
def stage_paises(ronda:str):
    q = db["paises"].find({"Stage": ronda.capitalize()},{"_id":0, "Teams":1}) 
    return loads(json_util.dumps(q))

@router.get("/info/goals_favour_per_game/{pais}") #nos todos los goles por partido de cada pais(todos)
def goals_per_game(pais):
    q = list(db["paises"].find({"Teams": pais.capitalize()},{"_id":0, "Goals favour per game":1}))
    return loads(json_util.dumps(q))    

#@router.get("/paises") #en la ruta hay que escribir /paises?pais=Spain
#def nombre(pais:str):
    #q = db["paises_2"].find({"Teams": pais},{"_id":0})
    #return loads(json_util.dumps(q))

