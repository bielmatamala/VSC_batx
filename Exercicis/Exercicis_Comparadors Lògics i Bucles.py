import math
from math import pi
import random
from random import randrange
#Exercicis: Comparadors Lògics i Bucles

#Booleans i operadors de comparació
#exercici 1
a = 5
b = 10
print(a == b)
print(a < b)
print(a != b)
print("-----------------------------------------------------------------")

#exercici 2
a = True 
b = False
print(a and b)
print(not a)
print(not b)
print(a or b)
print( not a or b)
print( a and not b)
print( not ( a and b ))
print("-----------------------------------------------------------------")
a = True
b = False
c = True
print ((a or b)and c)
print ((a and b) or c)
print ((a and b)and c)
print (not (a or b) and c)
print ((a and not b ) and c)
print (not ((a or b) and not c))
print("-----------------------------------------------------------------")
#Condicionals (if, elif, else)
#exercici 3
te_clau = True
porta_tancada = False
if te_clau == True and porta_tancada == False:
    print("Pot entrar a casa")
else:
    print("No pot entrar a casa")

print("-----------------------------------------------------------------")
#exercici 4
y = int(input("Introdueix un número: "))
if (-5/3 <= y < pi):
    print("El número està dins de l'interval")
else:
    print("El número està fora de l'interval")

print("-----------------------------------------------------------------")
#exercici 5
x = int(input("Introdueix un número: "))
if (x > 0):
    print("El número és positiu")
elif (x < 0):
    print("El número és negatiu")
else: 
    print("El nombre es igual a 0")
print("-----------------------------------------------------------------")

#exercici 6
edat = int(input("Introdueix la teva edat: "))
if (edat < 18):
    print("Ets menor d'edat")
else:
    print("Ets major d'edat")

#exercici 7
print("-----------------------------------------------------------------")
nota = int(input("La teva nota:"))
if nota < 5:
    print("has suspès")
elif nota >= 5 and nota <= 6.9 :
    print("Aprovat")
elif nota >= 7 and nota <= 8.9:
    print("Notable")
else:
    print("Execelent")

#exercici 8
print("-----------------------------------------------------------------")
for i in range(11):
    print(i, i**2, i**3)

#exercici 10
print("-----------------------------------------------------------------")
noms = ["joan", "marc"]
for n in noms:
    print(f"benvigut {n}")

#exrcici 11 
print("-----------------------------------------------------------------")
r = randrange(150)
while True:

    print(r)
    intents = 0
    if r < 150:
        r += 1
    else:
        print("radnom 150")
        break
    
    if intents >= 10:
        print("masses intents")
        break
    intents += 1

#exrcici 12
print("-----------------------------------------------------------------")
user_input_cT = True 
contrasenya = "python"
while user_input_cT == True:
    user_input_c = input("Introduix un contrasenya: ")
    if user_input_c == contrasenya:
        print("Contrasenya correcta")
        break
    else:
        print("Contrsanya incorecta")   

#exercici 13
print("-----------------------------------------------------------------")
llista_sum = []
user_inpput_1B = True
while user_inpput_1B != False:
    user_inpput_1 = int(input("introduix un nombre: "))
    llista_sum.append(user_inpput_1)
    print(sum(llista_sum))
    if user_inpput_1 == 0:
        user_inpput_1B = False
    else:
        user_inpput_1B = True
    
#~exercic 14
print("-----------------------------------------------------------------")
a = [23,1]
b = [23, 78, 9, 5, 6]
c = []
grau = len(b)-1
print(grau)