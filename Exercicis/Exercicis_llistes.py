# Exercici: obtenir ['H!','O!','L!','A!'] amb list comprehension
a = "Hola"
b = "!"
resultat = [lletra.upper() + b for lletra in a]
print(resultat)
## primer exercici
Llista1 = [1, 2, 3, 4, 5]
print(Llista1[0])
print(Llista1[-1])

## segon exercici
colors = ['vermell', 'verd', 'blau']
colors.append('groc')
print(colors)
colors.insert(1,"negre")
print(colors)
colors.remove('verd')
print(colors)


## tercer exercici
A = [1, 2, 3]
B = [4, 5]
C = A + B
print(C)

## quart exercici
llista2 = [0] * 1000

## cinquè exercici
nums = [10,20,30,40]
nums.remove(20)
nums.insert(1,99)
print(nums)
print(len(nums))
print(nums[-1])

## sisè exercici
l = [5,6,7,8,9,10]
print(l[0:3])
print(l[2:6])
print("hola")
print(l[::2])
print(l[-1:0:-1])
print(l[-2:0:-1])
print(l)

## setè exercici
paraula = "Barcelona"
llista3 = [lletra for lletra in paraula ]
print(llista3)

## vuitè exercici
a = "hola"
b = "!"
llista4 = [lletra.upper() + b for lletra in a]
print(llista4)

## nove exercici
noms2 = ["Anna","Marc","Pau","Júlia","Pau","Marc"]
print(noms2.index("Marc"))
 