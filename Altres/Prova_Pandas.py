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
print("----------------------------------------------------")
df_3 = pd.read_csv("https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesteroles.csv", sep=";", header=0, index_col=0)
print(df_3)
print("----------------------------------------------------")
"""
df_4 = df_3.to_csv("colesteroles_modificat.csv", sep=";", header=True, index=True) #serveix per exportar el dataframe a un fitxer csv, amb les opcions de separador, si volem que inclogui els noms de les columnes i si volem que inclogui els indexos, en aquest cas el nom del fitxer es "colesteroles_modificat.csv"
print(df_4)
print("----------------------------------------------------")
df_5 = df_3.to_csv("colesteroles_modificat_1.csv", sep=";", header=True, index=False) #serveix per exportar el dataframe a un fitxer csv, amb les opcions de separador, si volem que inclogui els noms de les columnes i si volem que inclogui els indexos, en aquest cas el nom del fitxer es "colesteroles_modificat_1.csv"
print(df_5)
print("----------------------------------------------------")
df_6 = df_3.to_csv("colesteroles_modificat_2.csv", sep=";", header=False, index=False) #serveix per exportar el dataframe a un fitxer csv, amb les opcions de separador, si volem que inclogui els noms de les columnes i si volem que inclogui els indexos, en aquest cas el nom del fitxer es "colesteroles_modificat_2.csv"
print(df_6)
"""
print("----------------------------------------------------")
print("----------------------------------------------------")
print(df_3.info())
print("----------------------------------------------------")
print(df_3.shape)
print("----------------------------------------------------")
print(df_3.size)
print("----------------------------------------------------")
print(df_3.columns)
print("----------------------------------------------------")
print(df_3.index)
print("----------------------------------------------------")
print(df_3.dtypes)
print("----------------------------------------------------")
print(df_3.head(3))
print("----------------------------------------------------")
print(df_3.tail(2))
print("----------------------------------------------------")
df_7 =df_3.rename(columns={"colesterol":"CT"})
print(df_7)
print("----------------------------------------------------")
df_8 = df_3.set_index(keys = "edad", verify_integrity = True) #serveix per canviar l'index del dataframe, en aquest cas es canvia l'index a la columna "edad", amb l'opcio de verificar que els valors de la columna "edad" siguin únics per evitar problemes d'indexos duplicats
print(df_8)
print("----------------------------------------------------")