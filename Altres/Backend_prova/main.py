import os
from fastapi import FastAPI 
from os import path
from fastapi.responses import FileResponse
import uvicorn

# 192.168.232.167 

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI!"}
def transf_file(fitxer_nom,extensio):
    @app.get("/transf")
    async def transf_file(fitxer_nom,extensio):
        fitxer = r"C:\Users\AppJT\VSC_batx\Backend_prova\transferencia_fitxers"+fitxer_nom+extensio
        if path.exists(fitxer):
            print("el fitxer existeix")
        else:
            print("el fitxer no existeix")
    return transf_file
        
if __name__ == "__main__":
    uvicorn.run(app, host="192.168.232.167", port=8000)