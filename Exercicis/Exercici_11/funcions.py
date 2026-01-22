import os
from pathlib import Path

class Gestor_Fitexers:
    def __init__ (self, directori):
        self.dir = Path(directori)
    
    def comprovar_directori(self):
        if self.dir.exists() and self.dir.is_dir():
            print("El directori existeix")
            return True
        else:
            print("El directori no existeix")
            return False
    
    def crear_directori(self):
        if self.comprovar_directori() == False:
            try:
                os.mkdir(self.dir)
                print("Directori creat")
            except Exception as e:
                print(f"Error al crear el directori: {e}")
        else:
            pass
    
    def crear_fitxer(self, nom_fitxer):
        Ubicacio = self.dir / nom_fitxer
        if not Ubicacio.exists():
            fitxerop = open(Ubicacio, "w")
            fitxerop.close()
            print("Fitxer creat")
        else:
            print("El fitxer ja existeix")

    def llista_fitxers(self, extencio=None):
        fitxer = self.dir.iterdir()
        ll_FITXERS = []
        for f in fitxer:
            if f.is_file():
                if extencio:
                    if f.suffix == extencio:
                        ll_FITXERS.append(f.name)
                    else:
                        pass

    def compta_fitxers(self, extencio=None):  
        fitxer = self.dir.iterdir()
        counter = 0
        for f in fitxer:
            if f.is_file():
                if extencio:
                    if f.suffix == extencio:
                        counter += 1
                    else:
                        pass
                else:
                    counter += 1
        return counter
    
    def escriu_text(self, fitxer, text, MOF = "a"):
        Ubicacio = self.dir / fitxer
        try:
            fitxerop = open(Ubicacio, MOF)
            fitxerop.write(text)
        except FileNotFoundError:
            print("El fitxer no existeix")

    def tancar_fitxer(self, fitxer):
        Ubicacio = self.dir / fitxer
        try:
            fitxerop = open(Ubicacio, "a")
            fitxerop.close()
            print("Fitxer tancat")
        except FileNotFoundError:
            print("El fitxer no existeix")