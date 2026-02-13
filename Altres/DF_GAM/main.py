import pandas as pd
from DF import DF_GAM
df = DF_GAM()
print(df)

for Gimnasta in df["Gimnasta"]:
    pos_gim  = df.index[df["Gimnasta"] == Gimnasta][0]
    NT = df.loc[pos_gim, "Total"]
    print(f"Gim: {Gimnasta}, Total: {NT}")
    NT = 0