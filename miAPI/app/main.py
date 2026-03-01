#importaciones
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
import asyncio
from typing import Optional

class agregar_usuario(BaseModel):
    id: int
    nombre: str
    edad: int

#Instancia del servidor
app = FastAPI(
    title= "Mi primer API",
    description= "Angel Joshua Guerrero Lozano",
    version="1.0"
)

usuarios=[
    {"id":1,"nombre":"Fany","edad":21},
    {"id":2,"nombre":"Aly","edad":21},
    {"id":3,"nombre":"Dulce","edad":21},
]

#Endspoints
@app.get("/")
async def holamundo():
    return {"mensaje":"Hola Mundo FastAPI"}

@app.get("/bienvenido")
async def bienvenido():
    await asyncio.sleep(5)
    return {"mensaje":"Bienvenido a FastAPI",
            "estatus":"200",
            }

@app.post("/v1/usuarios/", tags=['CRUD HTTP'] ,status_code=status.HTTP_201_CREATED)
async def crear_usuario(usuario:agregar_usuario):  #<-------- Usamos el modelo
    for usr in usuarios: 
        if usr ["id"] == usuario.id:
            raise HTTPException(
                status_code=400,
                detail= "El id ya existe"
            )
    usuarios.append(usuario) #<----------------- Convertimos el modelo a dict para agregarlo a la lista
    return{
        "mensaje":"Usuario Agregado",
        "Datos nuevos": usuario
    }

@app.get("/v1/parametroOb/{id}",tags=['Parametro Obligatorio'])
async def consultauno(id:int):
    return{ "mensaje": "usuario encontrado",
            "usuario": id,
            "status": "200"}
    
@app.get("/v1/parametro0p/", tags=['Parametros Opcionales'])
async def consultados(id: Optional[int] = None):
    if id is not None:
        for usuarioK in usuarios:
            if usuarioK["id"] == id:
                return {"mensaje": "usuario encontrado", "usuario": usuarioK}
            return {"mensaje": "usuario no encontrado", "satus": "200"}
    else:
        return {"mensaje": "No se propcionó un id", "status": "200"}

#GET
@app.get("/v1/usuarios/", tags=['HTTP CRUD'])
async def leer_usuarios():
    return {
        "total": len(usuarios),
        "usuarios": usuarios,
        "status": "200"
    }

# POST
@app.post("/v1/usuarios/", tags=['HTTP CRUD'])
async def agregar_usuario(usuario: dict):
    for usr in usuarios: 
        if usr["id"] == usuario.get("id"):
            raise HTTPException(
                status_code= 400,
                detail="El id ya existe"
            )
        
    usuarios.append(usuario)
    return{
        "mensaje": "Usuaruo creadie",
        "Datos nuevos"  : usuario
    }