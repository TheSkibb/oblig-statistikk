import pandas as pd
import numpy as np

"""
Hva er gjennomsnittlig dagsforbruk av romvarme disse to månedene? Hva er standardavviket?
"""

# bruker kode fra forrige oppgave for lasting av csv fil
varme = pd.read_csv("./varme.csv")
varme["Timestamp"] = pd.to_datetime(varme["Timestamp"], format="%d-%b-%y %H:%M:%S")

# filtrer til kun juli og juni
varme_jan = varme[(varme['Timestamp'] > "2018-01-01") & (varme['Timestamp'] < "2018-01-31")]
varme_jul = varme[(varme['Timestamp'] > "2018-07-01") & (varme['Timestamp'] < "2018-07-31")]

# sum per dag
varme_per_dag_jan = varme_jan.groupby(varme_jan['Timestamp'].dt.floor('D'))['Value (MW-hr)'].sum().reset_index(name='Value (MW-hr)')
varme_per_dag_jul = varme_jul.groupby(varme_jul['Timestamp'].dt.floor('D'))['Value (MW-hr)'].sum().reset_index(name='Value (MW-hr)')

jan_gjen = np.mean(varme_per_dag_jan['Value (MW-hr)'])
print(f"den gjennomsnittlige varmen per dag i januar er {jan_gjen} megawatt-timer")

jan_std = np.std(varme_per_dag_jan['Value (MW-hr)'], ddof=1)
print(f"standardavviket i januar er {jan_std}")

juli_gjen = np.mean(varme_per_dag_jul['Value (MW-hr)'])
print(f"den gjennomsnittlige varmen per dag i juli er {juli_gjen} megawatt-timer")

jul_std = np.std(varme_per_dag_jul['Value (MW-hr)'])
print(f"standardavviket i januar er {jul_std}")
