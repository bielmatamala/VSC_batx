#simple server
import http
from fastapi import FastAPI
import os
import http
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
async def HW():
    return "Hello, World!"

@app.get("/doc_1")
async def documentation():
    return RedirectResponse(url="http://127.0.0.1:8000/docs")

@app.get("/doc_2")
async def documentation_2():
    return RedirectResponse(url="http://127.0.0.1:8000/redoc")

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc
# Inicia el server: uvicorn main:app --reload
