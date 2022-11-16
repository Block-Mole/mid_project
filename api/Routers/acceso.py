from fastapi import APIRouter
from Database.mongodb import db
from bson import json_util #transformar json porque al hacer la llamada nos da un bson mo un json
from json import loads #cargar en json

router = APIRouter()

@router.get("/paises/{pais}")
def nombre(pais:str):
    q = db["paises_2"].find({"Teams": pais},{"_id":0})
    return loads(json_util.dumps(q))

@router.get("/paises") #en la ruta hay que escribir /paises?pais=Spain
def nombre(pais:str):
    q = db["paises_2"].find({"Teams": pais},{"_id":0})
    return loads(json_util.dumps(q))


@router.get("/saludo/{name}")
def saludo(name):
    return {
        "saludo": name
    }
@router.get("/despedida/{name}")
def despedir(name):
    return{
        "despedir":name
    }
