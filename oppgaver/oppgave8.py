import pandas as pd
import matplotlib.pyplot as plt

"""
Lag varighetskurver for romoppvarming og kjøling.
"""

varme = pd.read_csv("./varme.csv")
kulde = pd.read_csv("./kulde.csv")

varme["Timestamp"] = pd.to_datetime(varme["Timestamp"], format="%d-%b-%y %H:%M:%S")
varme['dag'] = varme['Timestamp'].dt.to_period('D')
dager_v = varme.groupby("dag").tail(1)
dager_v.loc[:,"Value (MW-hr)"] = dager_v['Value (MW-hr)'].diff()

kulde["Timestamp"] = pd.to_datetime(kulde["Timestamp"], format="%d-%b-%y %H:%M:%S")
kulde['dag'] = kulde['Timestamp'].dt.to_period('D')
dager_k = kulde.groupby("dag").tail(1)
dager_k.loc[:,"Value (MW-hr)"] = dager_k['Value (MW-hr)'].diff()

plt.plot(sorted(dager_k["Value (MW-hr)"], reverse=True), label="kjøling")
plt.plot(sorted(dager_v["Value (MW-hr)"], reverse=True), label="varme")
plt.ylabel("MW-hr")
plt.legend()
plt.show()
