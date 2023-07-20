#Importo le librerie utili
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import *


#Inizializzo la sessione e carico i dati
spark = SparkSession.builder.appName("LavoroFinale").getOrCreate()
df = spark.read.csv('lavoro_gruppo.csv', header=True, inferSchema=True)
df.orderBy('data_operazione').show(10)

#tipizzazione variabili
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

stat_descrittive = df.groupBy('anno_operazioni').agg(mean(round(abs('variazione'),2)).alias('media del valore operazioni per mese'),
                                                  median(abs('variazione')).alias('mediana del valore operazioni per mese'),
                                                  min(abs('variazione')).alias('operazione eseguita dal valore minore'),
                                                  max(abs('variazione')).alias('operazione eseguita dal valore minore')).sort('anno_operazioni',ascending=False)
stat_descrittive.show(10)


#Ritorno in formato Pandas, prima manipolazione
df_pd= df.toPandas() 
df_pd.drop('_c0',axis=1, inplace=True)
df_pd.drop('num_telefono',axis=1, inplace=True)
df_pd[['data_operazione','data_nascita','anno_nascita','anno_operazioni']].apply(pd.to_datetime)

#colonna rappresentante la comulativa della variabile variazione
df_pd['cum_variazione']=df_pd['variazione'].cumsum()

## Visualizzazione- Attività della Banca
#Analisi grafica
sns.relplot(x='anno_operazioni',y='cum_variazione', data=df_pd,kind='line')
plt.title('Evoluzione del valore totale dei depositi gestiti')
plt.xlabel('Anno di esercizio')
plt.ylabel('')

#operazioni gestite per periodo, tramite soglia
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

## Visualizzazione- Attività Clienti

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


# Analisi comportamento per generazioni di clienti
df_generazioni=df_pd

def assegna_generazione(anno):
  '''
  Implementa un ciclo if else
  
  Args:
      anno = valore int di partenza
  Returns:
      'Z','Y','X','Boomers'

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
