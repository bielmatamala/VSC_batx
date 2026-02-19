import pandas as pd
from DF import DF_GAM

df = DF_GAM()
print(df)

"""for Gimnasta in df["Gimnasta"]:
    pos_gim  = df.index[df["Gimnasta"] == Gimnasta][0]
    NT = df.loc[pos_gim, "Total"]
    print(f"Gim: {Gimnasta}, Total: {NT}")"""
NT = df["Total"]
NE = NT - df["Nota_D"]
print(f"NT: {NT}, NE: {NE}")
#s'ha de fer que segons el element fet (que te una nota_d), es miri si val la pena fer aquest elemnt si potser un de menys dificultat (nota_d) pots treure millor pntuacio pq la porbalilitat de fero malament es mes baixa.