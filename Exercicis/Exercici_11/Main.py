from pathlib import Path 
import os
from funcions import Gestor_Fitexers

ftx = Gestor_Fitexers(r".\Exercici_11\prova")
ftx.comprovar_directori()
ftx.crear_directori()
ftx.crear_fitxer("fitxer1.txt")
for i in range(10):
    if i <= 10:
        ftx.escriu_text("fitxer1.txt", f"Linia numero {i+1}" + f"{(((i+1)*100)-200)*0.5}\n")
    else:
        ftx.tancar_fitxer("fitxer1.txt")