from fastapi import FastAPI
from Routers import acceso

app = FastAPI()
app.include_router(acceso.router)

@app.get("/")
def inicio():
    return{
        "message": "Este es mi projecto de mitad de bootcam"
    }

