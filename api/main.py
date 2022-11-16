from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def inicio():
    return{
        "message": "prueba 1"
    }
@app.get("/query")
def query(name):
    return {
        "name":name
    }
@app.get("saludar/{name}")
def saludar(name):
    return {
        "saludo": name
    }