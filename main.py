import datetime
import banca
import funzioni
from archivio import lista_utenti
import getpass
import time


# Stampa del messaggio di benvenuto
funzioni.stampa_simulata("Ciao! Benvenuto nella banca PyBanking!\n")
time.sleep(0.7)
# Finestra operativa che consente all'utente di scegliere l'operazione da effettuare
operazione = input("Digita 1 se vuoi eseguire l'accesso \nDigita 2 se vuoi effettuare \
la registrazione \nDigita 3 se vuoi uscire \n")

while operazione != "3":
    
    # L'utente sceglie di eseguire l'accesso, digitando 1
    if operazione == "1":

        check_utente = 0    # variabile di controllo
        while check_utente == 0:
            utente = input("Inserisci il codice utente oppure digita INDIETRO per tornare \
alla pagina principale: ")

            # Stampa della finestra principale nel caso in cui l'utente abbia digitato INDIETRO
            if utente.lower() == "indietro":
                check_utente = 1
                operazione = input("Digita 1 se vuoi eseguire l'accesso \nDigita 2 se vuoi \
effettuare la registrazione \nDigita 3 se vuoi uscire \n")
            else:
                # Verifica dell'esistenza del codice utente nell'archivio della banca
                utente_trovato = 0
                for i in range(len(lista_utenti)):
                    if int(utente) == lista_utenti[i].utente:
                        utente_trovato = 1  # variabile di controllo
                        funzioni.stampa_simulata("Codice utente esistente.\n")
                        check_utente = 1
                        utente_attuale = lista_utenti[i]     # codice dell'utente attuale
                        break
                
                # Se il codice utente inserito non è presente in archivio, è possibile inserire un
                # nuovo codice utente oppure tornarte indietro per effettuare la registrazione
                if utente_trovato == 0:
                    funzioni.stampa_simulata("Codice utente non presente nel registro. Riprova oppure torna indietro per \
registrarti!\n")
                    check_utente = 0
        
        # Verificato il codice utente, si procede alla verifica della password
        if utente.lower() != "indietro":
            numero_tentativi = 0 # contatore sul numero di tentativi effettuati per l'inserimento password
            check_password = 0  # variabile di controllo sull'esattezza della password
            
            # Viene richiesto l'inserimento della password per al massimo tre volte
            while check_password == 0 and numero_tentativi < 3:
                password = getpass.getpass("Inserisci la password: ")
                numero_tentativi += 1
                check_password = utente_attuale.passwordCorretta(password)
                if check_password == 0:
                    print(f"Password errata! Tentativi rimasti {3-numero_tentativi}")
            
            # Esauriti i tre tentativi per l'inserimento della password, l'esecuzione viene interrotta.
            if numero_tentativi == 3 and check_password == 0:
                funzioni.stampa_simulata("Tentativi terminati\n")
                break
            else:
                # Si procede con la scelta dell'operazione da effettuare
                funzioni.stampa_simulata("Autenticazione eseguita con successo!\n")
                print("Il tuo saldo attuale è", utente_attuale.saldo,"€ \n")

                condizione_uscita = 0 # variabile di controllo
                while condizione_uscita !=1:
                    azione = input("Hai a disposizione le seguenti opzioni:\n \
    1 --> Deposito \n \
    2 --> Prelievo \n \
    3 --> Trasferimento di denaro\n \
    4 --> Stampa report \n \
    5 --> Esci\n \
Digita il numero corrispondente all'opzione desiderata: ")

                    # deposito
                    if azione == "1":
                        deposito = input("Hai scelto di depositare: quanto vuoi depositare? \
Digita MENU per tornare indietro.\n")
                        inserimento_corretto = 0 # variabile di controllo sull'esattezza del valore
                                                 # inserito come cifra di deposito
                        while inserimento_corretto != 1 and deposito.lower() != "menu" :
                            if not deposito.isdigit():
                                # Il valore inserito non contiene solo cifre, per cui non è valido
                                deposito = input("Inserimento non valido. Inserisci nuovo importo: ")
                            else:
                                utente_attuale.deposita(int(deposito))
                                inserimento_corretto = 1

                    # prelievo
                    elif azione == "2":
                        prelievo = input("Hai scelto di prelevare: quanto vuoi prelevare? \
Digita MENU per tornare indietro.\n")
                        inserimento_corretto = 0 # variabile di controllo sull'esattezza del valore 
                                                 # inserito come cifra di prelievo
                        while inserimento_corretto != 1 and prelievo.lower() != "menu":
                            if not prelievo.isdigit():
                                # Il valore inserito non contiene solo cifre, per cui non è valido
                                prelievo = input("Inserimento non valido. Inserisci nuovo importo: ")
                            elif int(prelievo) > utente_attuale.saldo:
                                # La cifra che si vuole prelevare è superiore al saldo disponibile
                                prelievo = input("Il saldo non è sufficiente! Inserisci nuovo importo: ")
                            else:
                                utente_attuale.preleva(int(prelievo))
                                inserimento_corretto = 1

                    # trasferimento di denaro
                    elif azione == "3":
                        funzioni.stampa_simulata("Hai scelto di trasferire denaro: a chi vuoi trasferire i soldi? \
Digita MENU per tornare indietro.\n")
                        # Viene richiesto l'inserimento del codice utente del destinatario
                        destinatario = input("Inserisci il codice utente del destinatario: ")
                        destinatario_trovato = 0 # variabile di controllo sull'esistenza del destinatario
                        while destinatario_trovato != 1 and destinatario.lower() != "menu":
                            for i in range(len(lista_utenti)):
                                if int(destinatario) == lista_utenti[i].utente:
                                    destinatario_trovato = 1
                                    funzioni.stampa_simulata("Il destinatario è nella lista utenti.\n")
                                    destinatario_attuale = lista_utenti[i] #codice utente del beneficiario
                                    break
                            if destinatario_trovato == 0:
                                funzioni.stampa_simulata("Codice utente non presente nel registro. Riprova!")
                                destinatario = input("Inserisci il codice utente del destinatario: ")

                        # Nel caso di codice utente valido per il destinatario, viene richiesto l'importo
                        # del trasferimento, sul quale viene effettuata una verifica sulla correttezza    
                        if destinatario_trovato == 1:
                            trasferimento = input("Inserisci l'importo che vuoi trasferire: ")
                            inserimento_corretto = 0
                            while inserimento_corretto != 1:
                                if not trasferimento.isdigit():
                                    trasferimento = input("Inserimento non valido. Inserisci nuovo \
importo: ")
                                elif int(trasferimento) > utente_attuale.saldo:
                                    trasferimento = input("Il saldo non è sufficiente! \
Inserisci nuovo importo: ")
                                else:
                                    inserimento_corretto = 1
                                    # L'importo desiderato viene trasferito dal conto dell'utente verso il
                                    # conto del beneficiario
                                    utente_attuale.trasferisci(int(trasferimento))
                                    destinatario_attuale.ricevi(int(trasferimento))

                    # stampa del report
                    elif azione == "4":
                        funzioni.stampa_simulata("Hai scelto di stampare il report")
                        utente_attuale.stampaReport()

                    # uscita
                    elif azione == "5":
                        funzioni.stampa_simulata("Hai scelto di uscire.")
                        condizione_uscita = 1
                        operazione = "3"


    elif operazione == "2":
        funzioni.stampa_simulata("Benvenuto nella procedura di registrazione!\n")

        # Inserimento e verifica del nome
        nome = input("Inserisci il tuo nome: ")
        nome = funzioni.controlloNome(nome)

        # Inserimento e verifica del cognome
        cognome = input("Inserisci il tuo cognome: ")
        cognome = funzioni.controlloCognome(cognome)

        # Inserimento e verifica dell'anno di nascita
        anno_di_nascita = input("Inserisci il tuo anno di nascita: ")
        anno_di_nascita = funzioni.controlloAnno(anno_di_nascita)

        # Inserimento e verifica del mese di nascita
        mese_di_nascita = input("Inserisci il tuo mese di nascita: ")
        mese_di_nascita = funzioni.controlloMese(mese_di_nascita)
        
        # Inserimento e verifica del giorno di nascita
        giorno_di_nascita = input("Inserisci il tuo giorno di nascita: ")
        giorno_di_nascita = funzioni.controlloGiorno(giorno_di_nascita, mese_di_nascita, anno_di_nascita)

        # Composizione della data di nascita
        data_nascita = datetime.date(int(anno_di_nascita),int(mese_di_nascita),int(giorno_di_nascita))

        # Inserimento dell'indirizzo
        indirizzo = input("Inserisci il tuo indirizzo: ")

        # Inserimento e controllo del numero di telefono
        num_telefono = input("Inserisci il tuo numero di telefono: ")
        num_telefono = funzioni.controlloNumero(num_telefono)
        
        # Creazione credenziali utente e registrazione nell'archivio della banca
        nuovo_utente = banca.Utente(nome, cognome, data_nascita, indirizzo, num_telefono)
        numero_utenti = len(lista_utenti)
        nuovo_utente.creaCredenziali(numero_utenti)
        lista_utenti.append(nuovo_utente)

        funzioni.stampa_simulata("Procedura di registrazione terminata con successo!\n")
        nuovo_utente.stampaCredenziali()
        
        # Procedura cambio password
        funzioni.chiedeCambiaPassword(nuovo_utente)
        operazione = input("\nScegli la nuova operazione da effettuare:\nDigita 1 se vuoi eseguire \
l'accesso \nDigita 2 se vuoi effettuare una nuova registrazione \nDigita 3 se vuoi uscire \n")


    else:
        # Il valore inserito non corrisponde ad una scelta valida
        funzioni.stampa_simulata("Scelta non corretta\n")
        operazione = input("Digita 1 se vuoi eseguire l'accesso \nDigita 2 se vuoi effettuare \
la registrazione \nDigita 3 se vuoi uscire \n")



if operazione == "3":
    time.sleep(0.7)
    funzioni.stampa_simulata("Arrivederci!")