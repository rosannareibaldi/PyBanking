import pandas as pd
from archivio import lista_utenti


# creo una lista di dataframe che raccolga ordinatamente le operazioni effettuate da ogni singolo utente
lista_dataframes = []
for i in lista_utenti:
    lista_dataframes.append(pd.DataFrame(i.registro))


def concatDataframes(lista_df):
    '''
    Concatena una lista di df pandas in un unico nuovo df

    Args:
        lista_df= lista contente per ogni elemento un df

    Return:
        concat_df = pandas df

    '''
    concat_df = pd.DataFrame()  # DataFrame vuoto per la concatenazione

    for df in lista_df:
        concat_df = pd.concat([concat_df, df], ignore_index=True)

    return concat_df


# creo un df contenete tutte le operazioni gestite dal sistema bancario
df_operazioni = concatDataframes(lista_dataframes)
df_operazioni.columns = ['id', 'data_operazione',
                         'operazione', 'variazione', 'saldo']


def creaDfUtente():
    '''
    Crea un df pandas ove ogni riga conterrà le informaioni
    relative ad un un singolo Utente 

    Args:
        None

    Returns:
        df_utenti : pandas dataframe

    '''

    l_nome = []
    l_cognome = []
    l_data_nascita = []
    l_indirizzo = []
    l_num_telefono = []
    l_saldo = []
    l_utente = []
    l_provincia=[]

    for i in lista_utenti:

        l_nome.append(i.nome)

        l_cognome.append(i.cognome)

        l_data_nascita.append(i.data_nascita)

        l_indirizzo.append(i.indirizzo)

        l_num_telefono.append(i.num_telefono)

        l_saldo.append(i.saldo)

        l_utente.append(i.utente)
        
        
        l_provincia.append(i.provincia)


        diz = {'nome': l_nome,
               'cognome': l_cognome,
               'data_nascita': l_data_nascita,
               'num_telefono': l_num_telefono,
               'saldo': l_saldo,
               'id': l_utente,
               'indirizzo':l_indirizzo,
               'provincia':l_provincia
               }

    df_utenti = pd.DataFrame(diz)
    return df_utenti


df_utenti = creaDfUtente()


# creo un nuovo df che associa ad ogni operazione effettuta i dati dell'utente di riferimento
df_utenti_operazioni = pd.merge(df_utenti, df_operazioni, on='id')

# manipolo il df aggiungendo alcune colonne
df_utenti_operazioni['anno_nascita'] = pd.to_datetime(
    df_utenti_operazioni['data_nascita']).dt.year
df_utenti_operazioni['anno_operazioni'] = pd.to_datetime(
    df_utenti_operazioni['data_operazione']).dt.year
df_utenti_operazioni['mese_operazioni'] = pd.to_datetime(
    df_utenti_operazioni['data_operazione']).dt.month
df_utenti_operazioni.drop('saldo_x', axis=1, inplace=True)

#creo un file csv per effettuare il passaggio a Spark
df_utenti_operazioni.to_csv('lista_utenti_operazioni.csv', sep=',', header=True)
df_utenti.to_csv('lista_utenti.csv',sep=',',header=True)
df_operazioni.to_csv('lista_operazioni.csv',sep=',',header=True)
