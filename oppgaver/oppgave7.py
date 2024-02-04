import pandas as pd
import matplotlib.pyplot as plt

"""
Lag et histogram som viser forbruket av romvarme (i hele 2018).
"""

varme = pd.read_csv("./varme.csv")

varme["Timestamp"] = pd.to_datetime(varme["Timestamp"], format="%d-%b-%y %H:%M:%S")
varme['dag'] = varme['Timestamp'].dt.to_period('D')
dager_v = varme.groupby("dag").tail(1)
dager_v.loc[:,"Value (MW-hr)"] = dager_v['Value (MW-hr)'].diff()


dager_v.drop(dager_v.index[0]).plot.hist()
plt.ylabel("frekvens")
plt.xlabel("MW-hr")

plt.show()
