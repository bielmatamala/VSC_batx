#simple server
import http
from fastapi import FastAPI
import os
import http

app = FastAPI()

@app.get("/")
async def HW():
    return "Hello, World!"

@app.get("/documentation")
async def documentation():
    return "http://127.0.0.1:8000/docs"
    

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc
# Inicia el server: uvicorn main:app --reload
