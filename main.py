# main.py
from fastapi import FastAPI
from pydantic import BaseModel

# Creamos la aplicación. El título y la descripción aparecen en Swagger.
app = FastAPI(
    title="Mi primera API",
    description="API sencilla para aprender a desplegar con Docker + ngrok",
    version="1.0.0",
)

# Modelo de datos: define qué JSON espera recibir el endpoint POST
class Numeros(BaseModel):
    a: float
    b: float

# "Base de datos" en memoria, solo para practicar
tareas = []

# GET simple: comprueba que la API está viva
@app.get("/")
def raiz():
    return {"mensaje": "La API funciona"}

# GET con parámetro en la URL: /saludo/Julen
@app.get("/saludo/{nombre}")
def saludo(nombre: str):
    return {"mensaje": f"Kaixo, {nombre}!"}

# POST que recibe un JSON en el cuerpo: {"a": 2, "b": 3}
@app.post("/sumar")
def sumar(numeros: Numeros):
    return {"resultado": numeros.a + numeros.b}

# POST para añadir una tarea a la lista
@app.post("/tareas")
def crear_tarea(texto: str):
    tareas.append(texto)
    return {"tareas": tareas}

# GET para ver todas las tareas
@app.get("/tareas")
def listar_tareas():
    return {"tareas": tareas}