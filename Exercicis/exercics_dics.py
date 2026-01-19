#exrcici 1
cotxe = {
    "marca": "Seat",
    "model": "Ibiza",
    "any": 2010,
}
print(cotxe)
color = cotxe["color"] = "blau"
print(cotxe)
any = cotxe["any"] = 2015
print(cotxe)
del cotxe["color"]
print(cotxe)
print(len(cotxe))
print(list(cotxe.keys()))

#exrcici 2
alumne = {
    "nom": "Joan",
    "edat": 20,
    "notes": [2, 5, 7, 9]
}
print(alumne)
alumne["notes"].append(10)
print(alumne["notes"][1])
print(alumne)
nom2 = alumne["nom"] = "Maria"
print(alumne)
notes2 = sum (alumne["notes"]) / len(alumne["notes"])
alumne["mitjana"] = notes2
print(alumne)

#exrcici 3
preus = {
    "pa": 13,
    "llet": 2,
    "ou": 10,
}
print(preus)
print(preus["pa"])
preus["sucre"] = 5
print(preus)
llistapreus = list(preus.keys())
print(llistapreus)
llistapreus2 = list(preus.values())
print(llistapreus2)
print(max(llistapreus2))


#exercici 4
dades = {
    "nom": "",
    "edat": 0,
    "telefon": "",
    "adreça": "",
}
dades["nom"]  = input("Introdueix el teu nom: ")
dades["edat"]  = input("Introdueix la teva edat: ")
dades["telefon"]  = input("Introdueix el teu telefon: ")
dades["adreça"]  = input("Introdueix la teva adreça: ")
print(f"El teu nom és {dades['nom']}, tens {dades['edat']} anys, el teu telefon és {dades['telefon']} i vius a {dades['adreça']}")




#exercici 5
credits = {
    "matematica": 6,
    "fisica": 4,
    "quimica": 5,
}
credits2 = [a for a in credits.keys()]
print(credits2)
print(f"{credits2[0]} te {credits[credits2[0]]} credits")
print(f"{credits2[1]} te {credits[credits2[1]]} credits")
print(f"{credits2[2]} te {credits[credits2[2]]} credits")




#exercici 6
agenda = {
    "Joan": {"telf": 123456789, "adreça": "Carrer de la Pau, 1"},
    "Maria": {"telf": 987654321, "adreça": "Avinguda del Mar, 5"},
}
print(agenda["Joan"])
print(agenda["Maria"])




#exercici 7
classe = {
    "Joan": {"edat": 20, "notes": [5, 7, 8]},
    "Maria": {"edat": 21, "notes": [6, 9, 10]},
}
# Afegir un alumne nou
classe["Pau"] = {"edat": 19, "notes": [7, 8, 9]}
print(classe)
# Mostrar la mitjana de notes d'un alumne concret
alumne = "Maria"
mitjana = sum(classe[alumne]["notes"]) / len(classe[alumne]["notes"])
print(f"La mitjana de notes de {alumne} és {mitjana}")
