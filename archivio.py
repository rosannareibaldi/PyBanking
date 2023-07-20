import datetime
import banca
import creazione
import random

# CREAZIONE LISTA UTENTI
lista_utenti = [] 


## GENERAZIONE MANUALE DI 3 UTENTI

# Utente1 
# utente = 1, password = "passsword"
data_nascita1 = datetime.date(1998, 12, 2)
utente1 = banca.Utente("Lucia", "Ferrari", data_nascita1, "via blabla", 3323458192,[[0, datetime.datetime(2023, 5, 20, 9, 13, 46, 63466), 'creazione conto', 0, 0],\
                                                                                     [0, datetime.datetime(2023, 5, 28, 9, 13, 46, 63466), 'deposito', 1000, 1000], \
                                                                                        [0, datetime.datetime(2023, 6, 10, 9, 13, 46, 63950), 'prelievo', -50, 950],\
                                                                                          [0, datetime.datetime(2023, 6, 12, 9, 13, 46, 63950), 'deposito', 20, 970], \
                                                                                            [0, datetime.datetime(2023, 7, 20, 9, 13, 46, 63950), 'prelievo', -200, 770]])
utente1.creaCredenziali(len(lista_utenti))
utente1.cambiaPassword("password")
lista_utenti.append(utente1)

# Utente 2
# utente = 2, password = "0000"
data_nascita2 = datetime.date(1994, 10, 23)
data_creazione2 = datetime.date(2020, 6, 9)
data_prelievo1 = datetime.date(2020, 7, 18)
utente2 = banca.Utente("Rosanna", "Reibaldi", data_nascita2, "via rosa", 37507872910, 2200, [[0, data_creazione2, "creazione conto", 2500, 2500],[0, data_prelievo1, "prelievo", - 300, 2200]])
utente2.creaCredenziali(len(lista_utenti))
utente2.cambiaPassword("0000")
lista_utenti.append(utente2)

# Utente 3
# utente = 3, password ="ciao"
data_nascita3 = datetime.date(1997, 4, 12)
data_creazione3 = datetime.date(2023, 3, 21)
utente3 = banca.Utente("Leonardo", "Brunetti", data_nascita3, "via tal dei tali", 3240432570, 5000, [[0, data_creazione3, "creazione conto", 5000, 5000]])
utente3.creaCredenziali(len(lista_utenti))
utente3.cambiaPassword("ciao")
lista_utenti.append(utente3)


## GENERAZIONE RANDOM DI 100 UTENTI

# Genero 100 nomi
lista_nomi = creazione.generaNomiPropri(100)

# Genero 100 cognomi
lista_cognomi = creazione.generaCognomi(100)

# Genero 100 date di nascita
lista_date_nascita = creazione.generaDateNascita(100)

# Genero 100 indirizzi
lista_indirizzi = creazione.generaIndirizzi(100)

# Genero 100 numeri di telefono
lista_num_telefono = creazione.generaNumeriTelefono(100)

# Genero 100 saldi 
lista_saldi = creazione.generaSaldi(100)

# Genero 100 registri di creazione e 100 utenti
for i in range(100):
    registro_creazione=[0,lista_date_nascita[i] + datetime.timedelta(days=18*365), "creazione conto", lista_saldi[i], lista_saldi[i]]
    registro = [registro_creazione]
    num_operazioni = random.randint(1,100)

    for j in range(num_operazioni):
        data_precedente = registro[len(registro)-1][1]
        saldo_precedente = registro[len(registro)-1][4]
        nuova_operazione = creazione.generaRegistro(data_precedente, saldo_precedente)
        registro.append(nuova_operazione)
    
    saldo_attuale = registro[len(registro)-1][4]    
    utente = banca.Utente(lista_nomi[i],lista_cognomi[i],lista_date_nascita[i],lista_indirizzi[i],lista_num_telefono[i],saldo_attuale,registro)
    utente.creaCredenziali(len(lista_utenti))
    lista_utenti.append(utente)

    # Per una questione dimostrativa, impostiamo una password identica per tutti, in modo da poter accedere dall'interfaccia. 
    # Senza questo comando le password sono generate random in precedenza.
    utente.cambiaPassword("1234") #Password = "1234"


