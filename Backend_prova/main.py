from fastapi import FastAPI 
from os import path
from fastapi.responses import FileResponse
import uvicorn

# 192.168.232.167 

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI!"}

@app.get("/transf")
async def transf_file(fitxer_nom,extensio):
    fitxer = r"C:\Users\AppJT\VSC_batx\Backend_prova\transferencia_fitxers"+fitxer_nom+extensio
    if path.exists(fitxer):
        print("el fitxer existeix")
    else:
        print("el fitxer no existeix")

if __name__ == "__main__":
    # Remember: 0.0.0.0 makes it accessible to other PCs
    uvicorn.run(app, host="0.0.0.0", port=8000)
