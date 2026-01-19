from datetime import datetime,date
from time import strptime
bd = {
    "Tallers": { 
        101 : {
            "nom" : "Robòtica amb micro-bits", 
            "tags" : ["Robotica", "infantil"],
            "edat_min" : 10,
            "accessible" : True,
            "requereix_material" : True, 
            "matreials" : ["Ordiandor", "Cables"], 
            "sessions" : [1, 2]
            },
        102 : {
            "nom" : "Experiments de quimica", 
            "tags" : ["ciencia", "Laboratiri"],
            "edat_min" : 12,
            "accessible" : False,
            "requereix_material" : True,
            "matreials" : ["probeta"],
            "sessions" : [102]
        }, 
        103 : {
            "nom": "contes de la natura",
            "tags" : ["natura", "familiar"],
            "edat_min" : 6, 
            "accessible" : True,
            "requereix_material" : False,
            "matreials" : ["Llibre"],
            "sessions" : [3, 4]
        },
    },
    "sessions" : {
        1: {
            "taller_id": 101,
            "dia": "2025-11-15",
            "franja": "10:00-11:30",
            "espai_id": 7,
            "aforament": 10,
            "inscripcions": [
                {"persona_id": 5001, "inscrit": True,  "cancelada": False},
                {"persona_id": 5002, "inscrit": False, "cancelada": False},
            ],


        },
        2: {
            "taller_id": 101,
            "dia": "2025-11-16",
            "franja": "12:00-13:30",
            "espai_id": 7,
            "aforament": 10,
            "inscripcions": [
                {"persona_id": 5004, "inscrit": True, "cancelada": False},
            ],
        },
        3: {
            "taller_id": 102,
            "dia": "2025-11-15",
            "franja": "11:00-12:00",
            "espai_id": 8,
            "aforament": 10,
            "inscripcions": [
                {"persona_id": 5002, "inscrit": True,  "cancelada": True},
                {"persona_id": 5005, "inscrit": True,  "cancelada": False},
            ],
        },
        4: {
            "taller_id": 103,
            "dia": "2025-11-16",
            "franja": "17:00-18:00",
            "espai_id": 9,
            "aforament": 10,
            "inscripcions": [
                {"persona_id": 5003, "inscrit": True,  "cancelada": False},
                {"persona_id": 5006, "inscrit": False, "cancelada": False},
            ],
        },
        5: {
            "taller_id": 103,
            "dia": "2025-11-17",
            "franja": "10:00-11:00",
            "espai_id": 9,
            "aforament": 10,
            "inscripcions": [],
        },
    },
    "perosones" : {
        5001: {"nom": "Nil", "edat": 11, "preferncies": ["robots"]},
        5002: {"nom": "Laia", "edat": 13, "preferncies": ["quimica", "experiments"]},
        5003: {"nom": "Oriol", "edat": 7, "preferncies": ["contes"]},
        5004: {"nom": "Marta", "edat": 15, "preferncies": ["tecnologia", "natura"]},
        5005: {"nom": "Pau", "edat": 12, "preferncies": ["ciencies"]},
        5006: {"nom": "Júlia", "edat": 9, "preferncies": ["natura"]},
    },
    "espais": {
        7: {"nom": "Aula 2.4", "accessible": True},
        8: {"nom": "Aula 2.7", "accessible": True},
        9: {"nom": "Laboratori", "accessible": False},
        10: {"nom": "Biblioteca", "accessible": True},
    }
    
}
inscrits_valids1 = 0
for inscripcions in bd["sessions"][1]["inscripcions"]:
    if inscripcions["inscrit"] == True and inscripcions["cancelada"] == False:
        inscrits_valids1  += 1
    else:
        inscrits_valids1  += 0
places_lliures1 = bd["sessions"][1]["aforament"] - inscrits_valids1
bd["sessions"][1]["places_lliures"] = places_lliures1
print(bd["sessions"][1]["places_lliures"])
print(inscrits_valids1)

inscrits_valids2 = 0
for inscripcions in bd["sessions"][2]["inscripcions"]:
    if inscripcions["inscrit"] == True and inscripcions["cancelada"] == False:
        inscrits_valids2  += 1
    else:
        inscrits_valids2  += 0
places_lliures2 = bd["sessions"][2]["aforament"] - inscrits_valids2
bd["sessions"][2]["places_lliures"] = places_lliures2
print(bd["sessions"][2]["places_lliures"])
print(inscrits_valids2)

inscrits_valids3 = 0
for inscripcions in bd["sessions"][3]["inscripcions"]:
    if inscripcions["inscrit"] == True and inscripcions["cancelada"] == False:
        inscrits_valids3  += 1
    else:
        inscrits_valids3  += 0
places_lliures3 = bd["sessions"][3]["aforament"] - inscrits_valids3
bd["sessions"][3]["places_lliures"] = places_lliures3
print(bd["sessions"][3]["places_lliures"])
print(inscrits_valids3)

inscrits_valids4 = 0
for inscripcions in bd["sessions"][4]["inscripcions"]:
    if inscripcions["inscrit"] == True and inscripcions["cancelada"] == False:
        inscrits_valids4  += 1
    else:
        inscrits_valids4  += 0
places_lliures4 = bd["sessions"][4]["aforament"] - inscrits_valids4
bd["sessions"][4]["places_lliures"] = places_lliures4
print(bd["sessions"][4]["places_lliures"])
print(inscrits_valids4)

inscrits_valids5 = 0
for inscripcions in bd["sessions"][5]["inscripcions"]:
    if inscripcions["inscrit"] == True and inscripcions["cancelada"] == False:
        inscrits_valids5  += 1
    else:
        inscrits_valids5  += 0
places_lliures5 = bd["sessions"][5]["aforament"] - inscrits_valids5
bd["sessions"][5]["places_lliures"] = places_lliures5
print(bd["sessions"][5]["places_lliures"])
print(inscrits_valids5)

user_input_Pl = int(input("De quina seessio vols mira les places lliures? (1-5): "))
print(bd["sessions"][user_input_Pl]["places_lliures"])

user_input_SD  = input("De quina dia vols saber les sessions? (format: yyyy-mm-dd) ")
data_input = datetime.strptime(user_input_SD, "%Y-%m-%d").date()
sessions_trobades = []
for sessio_id, sessio, in bd["sessions"].items():
        data_sessio = datetime.strptime(sessio["dia"], "%Y-%m-%d").date()
        if data_sessio == data_input:
            sessions_trobades.append(sessio_id)
if sessions_trobades == True:
    print(f"Sessions el {user_input_SD}: {sessions_trobades}")
else:
    print("No hi ha sessions aquesta data")

user_input_tag = input("Quin tag t'agrada? (Robotica, infantil, ciencia, Laboratiri, natura, familiar): ")
for tag in bd["Tallers"]:
    if user_input_tag in bd["Tallers"][tag]["tags"]:
        print(f"Taller amb el tag {user_input_tag}: {bd['Tallers'][tag]['nom']}")
        trobats = True
else:
    print("No hi ha tallers amb aquest tag")

user_input_SA = int(input("Quina sessio vols saber la seva accessibilitat? (1-5): "))
id_taller = bd["sessions"][user_input_SA]["taller_id"]
id_taller_accessibilitat = bd["Tallers"][id_taller]["accessible"]
id_espai = bd["sessions"][user_input_SA]["espai_id"]
id_espai_accessibilitat = bd["espais"][id_espai]["accessible"]
if id_taller_accessibilitat == True and id_espai_accessibilitat == True:
    print("La sessio es accessible")
else:
    print("La sessio no es accessible")

user_input_ST = int(input("Quin taller vols saber les seves sesions (101-103): "))
session_taller = []
for sessio_id, sessio in bd["sessions"].items():
    if sessio["taller_id"] == user_input_ST:
        session_taller.append(sessio_id)
print(f"Les sessions del taller {user_input_ST} son: {session_taller}")


user_input_IV = int(input("De quina sessio vols saber els inscrits valides? (1-5): "))
sessio = bd["sessions"][user_input_IV]
if "inscrits_valids" in sessio:
    print(f"Els inscrits valids de la sessio {user_input_IV} son: {sessio['inscrits_valids']}")
else:
    inscrits_valids = sum(1 for inscripcio in sessio["inscripcions"] if inscripcio["inscrit"] and not inscripcio["cancelada"])
    sessio["inscrits_valids"] = inscrits_valids
    print(f"Els inscrits valids de la sessio {user_input_IV} son: {inscrits_valids}")

user_input_PP = int(input("De quina persona vols saber els seus preferits? (5001-5006): "))
print(f"Les preferencies de la persona {user_input_PP} son: {bd['perosones'][user_input_PP]['preferncies']}")

user_input_SAP = int(input("quina sessions esta inscrit la persona? (5001-5006): "))
sessions_inscrit = []
for sessio_id, sessio in bd["sessions"].items():
    for inscripcio in sessio["inscripcions"]:
        if inscripcio["persona_id"] == user_input_SAP and inscripcio["inscrit"] == True and inscripcio["cancelada"] == False:
            sessions_inscrit.append(sessio_id)
print(f"La persona {user_input_SAP} esta inscrita a les sessions: {sessions_inscrit}")