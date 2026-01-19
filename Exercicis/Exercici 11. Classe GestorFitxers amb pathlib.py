from pathlib import Path 
import os

class Gestor_Fitexers:
    def __init__ (self, directori):
        self.dir = Path(directori)
        if directori not in os.listdir():
            os.mkdir(directori)
            if "fitxer_1.txt" not in os.listdir(directori):
                fitxer = open(directori + "\\fitxer_1.txt", "w")
                fitxer.write("Aquest és el fitxer 1.\n")
                fitxer.close()

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
        Ubicacio = self.dir
        try:
            fitxer in Ubicacio
            fitxerop = open(fitxer, MOF)
            fitxerop.write(text)
            fitxerop.close()
        except FileNotFoundError:
            print("El fitxer no existeix")

fitxer = Gestor_Fitexers("C:\\Users\\AppJT\\VSC_batx\\Exercicis\\Prova_Gestor_Fitxers")
print(fitxer.llista_fitxers(".txt"))
print(fitxer.compta_fitxers(".txt"))
fitxer.escriu_text("fitxer_1.txt", "\nAixò és una prova d'escriptura en un fitxer.", "w")
print(fitxer.llista_fitxers(".txt")) 
