import pandas as pd
import matplotlib.pyplot as plt

"""
Oppgave 1 :
Hva er totalforbruket av romvarme for 2018? Hva er totalforbruket for hver av årets 12 måneder? Vis resultatene som en graf.
"""
varme = pd.read_csv("./varme.csv")

varme["Timestamp"] = pd.to_datetime(varme["Timestamp"], format="%d-%b-%y %H:%M:%S")
varme.at[0, "Timestamp"] = varme.at[0, "Timestamp"] - pd.DateOffset(months=1)
varme['maaned'] = varme['Timestamp'].dt.to_period('M')
maaneder_v = varme.groupby('maaned').tail(1)
maaneder_v.loc[:, 'Value (MW-hr)'] = maaneder_v['Value (MW-hr)'].diff()
maaneder_v = maaneder_v.drop(0)

plt.plot(list(range(0, len(maaneder_v))), maaneder_v["Value (MW-hr)"])

plt.xlabel("dato")
plt.ylabel("forbruk MW-hr")
plt.xticks(list(range(0, 12)), ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
plt.grid()
plt.show()

plt.show

