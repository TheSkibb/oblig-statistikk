import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, DayLocator

"""
Oppgave 3

Statistikk for bergvarmeanlegg Oppvarming og kjøling av bygninger er en av de tre store driverne av klima- gassutslipp i verden, sammen med transport og industri. I det grønne skiftet trengs det grønne løsninger for bygninger, og gjerne løsninger som belaster elektrisitetsnettet minst mulig. Varmepumper vil være en del av dette bildet, men som vi nordboere vet går virkningsgraden til varmepumper ned når det blir kaldt ute og vi trenger varmen som mest. Bergvarme er en mulig løsning på dette problemet. Dypt nede holder grunnfjellet en jevn temperatur på rundt 4 °C året rundt. Energibrønner boret ned i grunnfjellet gir altså varmepumpen en jevn temperatur å arbeide mot hele året. Dataene som brukes i denne oppgaven kommer fra hotellet Scandic Flesland Airport på Flesland i Bergen. Vi skal se på et datasett for 2018 som inneholder data for mengden varme som er hentet ut til romoppvarming og mengden varme som ble ført tilbake i berget ved å kjøle ned inneluften om sommeren. Datafilene viser kumulativt energiforbruk siden oppstarten av anlegget, logget med en periode på 10 min. 1. Installer Python-biblioteket pandas og bruk det til å laste inn datafilene varme.csv og kulde.csv ved hjelp av funksjonen pandas.read_csv. Hint: Den første kolonnen i hver av datafilene inneholder tidspunkter. Det kan være nyttig å bruke argumentet parse_dates = ['Timestamp'] for at pandas skal tolke denne kolonnen som tidspunkter i stedet for strenger. 2. Hva er totalforbruket av romvarme for 2018? Hva er totalforbruket for hver av årets 12 måneder? Vis resultatene som en graf. Hint: pandas bruker en egen datatype som kalles datarammer. Bruk en for-løkke til å løpe over alle linjene i datarammen når du skal finne totalforbruket for hver av årets måneder. Du kan adressere en enkeltlinje i i datarammen df ved hjelp av syntaksen df.iloc[i]. Verdien i kolonne j kan hentes ut med df.iloc[i,j]. Månedsnummeret til et tidspunkt time er lagret i egenskapen month; syntaksen time.month gir altså månedsnummeret. Når du tegner grafen kan det være nyttig å bruke funksjonen matplotlib.pyplot.plot. Vi skal nå se litt nærmere på månedene januar og juli.

Hva er forbruket av romvarme for hver av dagene i disse månedene? 
Inspiser dagsforbruket for hver av disse to månedene ved hjelp av et spredningsplott.
Finnes det noen ekstreme verdier (outliers) i disse to månedene?
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

dager_jan.plot.scatter("Timestamp", "Value (MW-hr)")
plt.title("spredningsplot januar")
plt.gca().xaxis.set_major_locator(DayLocator())
plt.gca().xaxis.set_major_formatter(DateFormatter("%d"))
plt.grid()

dager_jul.plot.scatter("Timestamp", "Value (MW-hr)")
plt.title("spredningsplot juli")
plt.gca().xaxis.set_major_locator(DayLocator())
plt.gca().xaxis.set_major_formatter(DateFormatter("%d"))
plt.grid()

plt.show()

