import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Presenter forbruket i månedene januar og juli som et boksplott.
"""

varme = pd.read_csv("./varme.csv")

varme["Timestamp"] = pd.to_datetime(varme["Timestamp"], format="%d-%b-%y %H:%M:%S")
varme['dag'] = varme['Timestamp'].dt.to_period('D')
dager_v = varme.groupby("dag").tail(1)
dager_v.loc[:,"Value (MW-hr)"] = dager_v['Value (MW-hr)'].diff()

dager_jan = dager_v.loc[
(dager_v['Timestamp'] > "2018-01-01") & 
(dager_v['Timestamp'] < "2018-01-31")]
dager_jul = dager_v.loc[
(dager_v['Timestamp'] > "2018-07-01") & 
(dager_v['Timestamp'] < "2018-07-31")]

plt.boxplot([dager_jan["Value (MW-hr)"].drop(dager_jan.index[0]), dager_jul["Value (MW-hr)"]])
plt.xticks([1, 2], ["jan", "jul"])
plt.ylabel("MW-hr")
plt.title("varme januar og juli boksplot")

plt.show()


