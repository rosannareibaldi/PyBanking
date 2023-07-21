#Inizializzo la sessione e carico i dati
spark = SparkSession.builder.appName("LavoroFinale").getOrCreate()
df = spark.read.csv('lista_utenti_operazioni.csv', header=True, inferSchema=True)
df.orderBy('data_operazione').show(10)

#Importo le librerie utili
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import geopandas as gpd
import folium
from shapely.geometry import Point
from folium.plugins import MarkerCluster

#conversione tipo di variabili
from pyspark.sql.types import *
df = df.withColumn("data_nascita", col("data_nascita").cast(DateType()))
df=df.withColumn('num_telefono',col('num_telefono').cast(IntegerType()))
df=df.withColumn('variazione',col('variazione').cast(FloatType()))
df=df.withColumn('saldo_y',col('saldo_y').cast(FloatType()))
df =df.withColumn("data_operazione", col("data_operazione").cast(TimestampType()))

df.printSchema()

#numero righe e numero colonne
numero_righe=df.count()
numero_colonne=len(df.columns)
print(numero_righe,numero_colonne)
#numero clienti
numero_clienti=df.select('id').distinct().count()
#quante volte sono state processate le singole operazioni dalla banca
n_operazioni_tipo=df.groupBy('operazione').count()

#quanti soldi sono presenti ad oggi in banca?
cassa=df.agg({'saldo_y':'sum'}).collect()[0][0]

#statistiche descrittive
from pyspark.sql.functions import mean
#media del valore delle operazioni in ogni mese dell'anno

stat_descrittive = df.groupBy('anno_operazioni').agg(round(mean(abs('variazione')),2).alias('media del valore operazioni per anno'),
                                                  median(abs('variazione')).alias('mediana del valore operazioni per anno'),
                                                  min(abs('variazione')).alias('operazione eseguita con il valore minore'),
                                                  max(abs('variazione')).alias('operazione eseguita con il valore maggiore')).sort('anno_operazioni',ascending=True)
stat_descrittive.show(10)


#Ritorno in formato Pandas
df_pd= df.toPandas()
df_pd.drop('_c0',axis=1, inplace=True)
df_pd.drop('num_telefono',axis=1, inplace=True)
df_pd[['data_operazione','data_nascita','anno_nascita','anno_operazioni']].apply(pd.to_datetime)
df_pd['cum_variazione']=df_pd['variazione'].cumsum()

#apro il csv Lista Utenti e lo riduco alle colonne provincia e id
df1=pd.read_csv('lista_utenti')
df1 = df1[['provincia','id']]

#conto il numero di utenti per provincia
df2=df1.groupby('provincia').agg({'id':'nunique'}).reset_index()

print(df2.head(3))
print(len(df2))

print(df1.head(3))

#geolocalizzo le province tramite provider geopandas
città_geolocalizzate = gpd.tools.geocode(df2.provincia, provider="arcgis")
città_geolocalizzate['Latitude'] = città_geolocalizzate['geometry'].y
città_geolocalizzate['Longitude'] = città_geolocalizzate['geometry'].x

print(città_geolocalizzate.head(3))

città_geolocalizzate= città_geolocalizzate.sort_values('address')
print(len(città_geolocalizzate))

df2=df2.sort_values('provincia')
print(len(df2))
print(df2.head(3))

#aggiungo la colonna id
città_geolocalizzate['numero_clienti']= df2['id']
print(città_geolocalizzate.head(3))

#centro la mappa globale sulla regione italiana
italy_map = folium.Map(location=[41.90322, 12.49565], zoom_start=6)

#aggiungo un marker per ogni città in cui è presente un cliente
marker_cluster = MarkerCluster().add_to(italy_map)
for idx, row in città_geolocalizzate.iterrows():
    popup_text = f"address: {row['address']}<br>numero_clienti: {row['numero_clienti']}" #aggiungo il numero di clienti come attributo al marker
    folium.Marker(location=[row['geometry'].y, row['geometry'].x], popup=popup_text).add_to(marker_cluster)

italy_map

#ANALISI ESPLORATIVA 

sns.relplot(x='anno_operazioni',y='cum_variazione', data=df_pd,kind='line')
plt.title('Evoluzione del valore totale dei depositi gestiti')
plt.xlabel('Anno di esercizio')
plt.ylabel('')

#operazioni gestite per periodo

soglia= (df_pd['anno_operazioni'].max()) - int(input(''))

df_10a =df_pd[df_pd['anno_operazioni']>=soglia]

sns.countplot(data=df_10a,y='operazione')
plt.title('operazioni gestite nel periodo di riferimento')
plt.xlabel('')
plt.show()

sns.countplot(data=df_10a,y='operazione',hue='anno_operazioni')
plt.title('operazioni gestite nel periodo per anno di riferimeno')
plt.xlabel('')
plt.show()


#indagine su singolo cliente
id_analisi= int(input())

df_cliente=df_pd[df_pd['id']== id_analisi]

df_cliente.astype({'anno_operazioni': 'int32'}).dtypes

#df_cliente['anno_operazione']=df_cliente['anno_operazione'].astype('int')
print(df_cliente)

sns.countplot(data=df_cliente ,x='operazione')
plt.title('numero di operazioni effettuate dal cliente')
plt.ylabel('')
plt.xticks(rotation=90)
plt.show()

sns.relplot(x='anno_operazioni',y='cum_variazione', data=df_cliente, kind='line')
plt.xlabel('Anno di riferimento')
plt.ylabel('Disponibilità del cliente')
plt.title('Evoluzione delle disponibilità del cliente')
plt.xticks(rotation=90)
plt.show()


# Analisi per generazione con boxplot
df_generazioni=df_pd

def assegna_generazione(anno):
  '''

  '''
  if anno>=2000:
    return 'Z'
  elif anno <2000 and anno>1980:
    return 'Y'
  elif anno <= 1980 and anno>1960:
    return 'X'
  else:
    return 'Boomers'

df_generazioni['generazioni']= df_generazioni['anno_nascita'].apply(assegna_generazione)
df_generazioni['variazione_bool']= df_generazioni['variazione']>=0

sns.violinplot(data=df_generazioni, x="variazione", y="generazioni")
plt.title('Distribuzione della variazione per classe di clienti')
plt.show()

sns.countplot(data=df_generazioni, y='operazione', hue='generazioni')
plt.xlabel('')
plt.title('operazione gestite per classe di clienti')
plt.show()


spark.stop()
