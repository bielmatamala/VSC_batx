import math
#extres 1
dies_tupla = ('Dilluns', 'Dimarts', 'Dimecres', 'Dijous', 'Divendres', 'Dissabte', 'Diumenge')
bucle = True
while bucle:
    user_input_dia = int(input("Introdueix un número del 0 al 6 per veure el dia corresponent: "))
    if 0 <= user_input_dia <= 6:
        print(f"El dia corresponent és: {dies_tupla[user_input_dia]}")
    else:
        print("Número no vàlid.")
        bucle = False

print("-----------------------------------------------------------------")

#extrres 2
mesos_tupla = ('Gener', 'Febrer', 'Març', 'Abril', 'Maig', 'Juny', 'Juliol', 'Agost', 'Setembre', 'Octubre', 'Novembre', 'Desembre')
bucle_mes = True
while bucle_mes:
    user_input_mes = int(input("Introdueix un número de mes (1-12): "))
    if 1 <= user_input_mes <= 12:
        print(f"El mes correponent al teu nnumero és: {mesos_tupla[user_input_mes - 1]}")
        bucle_mes = True
    else:
        print("Número no vàlid.")
        bucle_mes = False

print("-----------------------------------------------------------------")

#extrres 3
user_input_parauala = str(input("Introdueix una paraula: "))
parauala = user_input_parauala.lower()
vocals = ('a', 'e', 'i', 'o', 'u', 'à', 'è', 'é', 'í', 'ò', 'ó', 'ú')
vocal = 0
for lletra in parauala:
    if lletra in vocals:
        print(f"La LLetra {lletra} és una vocal.")
        vocal += 1
    else:
        print(f"La LLetra {lletra} no és una vocal.")

print(f"El nombre de vocals és: {vocal}")

print("-----------------------------------------------------------------")

#extrres 4
user_input_nombre = input("Introdueix un número: ")
try: 
    diviso = 10/user_input_nombre
    print(f"El resultat de la divisió és: {diviso}")

except ZeroDivisionError:
    print("Error: No es pot dividir per zero.")

except user_input_nombre == str or TypeError:
    print("Error: Entrada no vàlida.")

print("-----------------------------------------------------------------")

#extrres 5
user_input_numero = input("Introdueix un número: ")
user_input_numero2 = input("Introdueix un altre número: ")
try:
    resultat = user_input_numero / user_input_numero2
    print(f"El resultat de la divisió és: {resultat}")
except ZeroDivisionError:
    print("Error: No es pot dividir per zero.")
except TypeError:
    print("Error: Entrada no vàlida.")
except ValueError:
    print("Error: Entrada no vàlida.")
except user_input_numero == str or user_input_numero2 == str:
    print("Error: Entrada no vàlida.")
except user_input_numero == float or user_input_numero2 == float:
    print("Error: Entrada no vàlida.")

print("-----------------------------------------------------------------")

#extrres 6
notes = ((5,7,8), (6,6,7), (9,8,10))
for alumne in notes:
    suma = sum(alumne)
    mitjana = suma / len(alumne)
    print(f"La mitjana de les notes de l'alumne és: {mitjana}")

print("-----------------------------------------------------------------")

#extrres 7
tupla_nombres = (16, 25, 36, 49, 64, 2, 3, 5, 7, 10)
user_input_nombre_tupla = int(input("Introdueix un número: "))
try:
    if user_input_nombre_tupla in tupla_nombres:
        print(f"El nombre {user_input_nombre_tupla} està a la tupla.")
except ValueError:
    print("Error: Entrada no vàlida.")
except TypeError:
    print("Error: Entrada no vàlida.")
else: 
    print(f"El nombre {user_input_nombre_tupla} no està a la tupla.")

print("-----------------------------------------------------------------")

#extrres 8
capitals = ("Barcelona","Girona","Tarragona","Lleida")
for ciutat in enumerate(capitals):
    print(ciutat)
print("-----------------------------------------------------------------")

#extrres 9
temp_celsius = (0, 20, 37, 67, 100)
temp_farenheits = tuple((celsius * 1.8) + 32 for celsius in temp_celsius)
print(temp_farenheits)
print("-----------------------------------------------------------------")

#extrres 10
productes = ((" Poma ", 3.5) , (" Platan ", 2.8) , (" Taronja ", 4.1) )
print(f"El producte més car és:{max(productes)}")
print(f"El preu mitja és de: {(sum(preu for _, preu in productes) / len(productes))}")
print("-----------------------------------------------------------------")

#extrres 11
import random
llista_nombres = []
user_input_n = int(input("Introdueix un número entre 0 i 100: "))
for x in range(100):
    n = random.randint(0, user_input_n)
    if n > 100 and x <= 100: 
        llista_nombres.append(n)
        print(f"La llista de nombres és: {llista_nombres}")
    else:
        pass
length = len(llista_nombres)  
min = 0
max = 1000
suma = 0
for a in llista_nombres:
    if a < min:
        min = a
    if a > max:
        max = a
    suma += a
mitjana = suma / length

print(f"El mínim és: {min}")
print(f"El màxim és: {max}")
print(f"La mitjana és: {mitjana}")
print(f"La suma és: {suma}")

print("-----------------------------------------------------------------")