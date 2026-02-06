import pandas as pd
"""Data_dict = {
    "nom": ["Alice", "Bob", "Charlie"],
    "edat": [25, 30, 35],
    "ciutat": ["Barcelona", "Madrid", "Valencia"],
    "ocupacio": ["Enginyer", "Metge", "Professor"]
}
Data_list = []
for key in Data_dict:
    Data_list.extend(Data_dict[key])
print(Data_list)
print("----------------------------------------------------")
s = pd.Series(data = Data_list)
print(s)
print("----------------------------------------------------")
q = pd.Series(data = Data_dict)
print(q)
print("----------------------------------------------------")
print(q.size)
print(q.index)
print(q.dtype)
print("----------------------------------------------------")
print(s.size)
print(s.index)
print(s.dtype)
print("----------------------------------------------------")
print(s[5])
print("----------------------------------------------------")
s = pd.Series([1, 1, 1, 1, 2, 2, 2, 3, 3, 4])
print(s.describe())"""

datos = {
    'nombre':['María', 'Luis', 'Carmen', 'Antonio'],
    'edad':[18, 22, 20, 21],
    'grado':['Economía', 'Medicina', 'Arquitectura', 'Economía'],
    'correo':['maria@gmail.com', 'luis@yahoo.es', 'carmen@gmail.com', 'antonio@gmail.com']
}
df = pd.DataFrame(data = datos, index=['a', '2', 'c', '4'], columns=['nombre', 'edad', 'grado', 'correo'], dtype='object')#quadricula de dades(dataframe), amb index personalitzats, colunes han de ser sempre les keys del dict
print(df)
print("----------------------------------------------------")
df2 = pd.DataFrame(data = datos)#quadricula de dades(dataframe), amb index predeterminats al no especificar-los, colunes han de ser sempre les keys del dict
print(df2)