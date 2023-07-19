import datetime
import registro

# messaggio di benvenuto
print("Ciao! Benvenuto nella banca PyBanking!")

# scelta dell'operazione che si vuole effettuare
operazione = input("Digita 1 se vuoi eseguire l'accesso \nDigita 2 se vuoi effettuare la registrazione \nDigita 3 se vuoi uscire \n")

while operazione != "3":

    if operazione == "1":   # accesso dell'utente


        check_utente = 0
        while check_utente == 0:
            utente = input("Inserisci il codice utente oppure digita INDIETRO per tornare alla pagina principale: ")

            if utente == "INDIETRO":
                check_utente = 1
            else:
                
                # verifica se l'utente è presente nella lista utenti
                utente_trovato = 0
                for i in range(len(registro.lista_utenti)):
                    if int(utente) == registro.lista_utenti[i].utente:
                        utente_trovato = 1
                        print("Codice utente esistente.")
                        check_utente = 1
                        utente_attuale =  registro.lista_utenti[i]
                        break
                if utente_trovato == 0:
                    print("Codice utente non presente nel registro. Riprova!")
                    check_utente = 0
        
        if utente != "INDIETRO":
            numero_tentativi = 0
            check_password = 0
            while check_password == 0 and numero_tentativi < 3:
                password = input("Inserisci la password: ")
                numero_tentativi += 1
                check_password = utente_attuale.passwordCorretta(password)
                if check_password == 0:
                    print("Password errata!")

            if numero_tentativi == 3 and check_password == 0:
                print("Tentativi terminati")
                break
            else:
                print("Autenticazione eseguita con successo!")
                print("Il tuo saldo attuale è", utente_attuale.saldo,"€")
                azione = input("Hai a disposizione le seguenti opzioni:\n \
                    1 --> Deposito \n \
                    2 --> Prelievo \n \
                    3 --> Trasferimento di denaro\n \
                    4 --> Stampa report \n \
                    5 --> Esci\n \
                Digita il numero corrispondente all'opzione desiderata: ")

                if azione == "1":
                    deposito = input("Hai scelto di depositare: quanto vuoi depositare? Digita MENU per tornare indietro.\n")
                    if deposito == "MENU":
                        break
                    elif not deposito.isdigit():
                        print("Inserimento non valido. Inserisci nuovo importo: ")
                    else:
                        deposito = int(deposito)
                        utente_attuale.deposita(deposito)


                elif azione == "2":
                    print("Hai scelto di prelevare")
                elif azione == "3":
                    print("Hai scelto di trasferire denaro")
                elif azione == "4":
                    print("Hai scelto di stampare il report")
                elif azione == "5":
                    print("Hai scelto di uscire")
                    break



    elif operazione == "2":
        print("Benvenuto nella procedura di registrazione!")
        nome = input("Inserisci il tuo nome: ")
        cognome = input("Inserisci il tuo cognome: ")
        anno_di_nascita = int(input("Inserisci il tuo anno di nascita nel formato 1990: "))
        mese_di_nascita = int(input("Inserisci il tuo mese di nascita nel formato 1,2,3...: "))
        giorno_di_nascita = int(input("Inserisci il tuo giorno di nascita nel formato 1,2,3...: "))
        data_nascita = datetime.date(anno_di_nascita,mese_di_nascita,giorno_di_nascita)
        indirizzo = input("Inserisci il tuo indirizzo: ")
        num_telefono = input("Inserisci il tuo numero di telefono: ")

        utente = registro.Utente(nome, cognome, data_nascita, indirizzo, num_telefono)

        numero_utenti = 56 # sistemare
        utente.creaCredenziali(numero_utenti)




    else:
        print("Scelta non corretta")

    # scelta dell'operazione che si vuole effettuare
    operazione = input("Digita 1 se vuoi eseguire l'accesso \nDigita 2 se vuoi effettuare la registrazione \nDigita 3 se vuoi uscire \n")





if operazione == "3":
    print("Arrivederci!")