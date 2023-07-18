liste_utenti = ["abc", "def"]

# messaggio di benvenuto
print("Ciao! Benvenuto nella banca PyBanking!")

# scelta dell'operazione che si vuole effettuare
operazione = input("Digita 1 se vuoi eseguire l'accesso \nDigita 2 se vuoi effettuare la registrazione \nDigita 3 se vuoi uscire \n")



if operazione == "1":   # accesso dell'utente


    check_utente = 0
    while check_utente == 0:
        utente = input("Inserisci il nome utente: ")


        # controllo sulla correttezza del nome utente
        if utente in liste_utenti:
            print("utente esistente")
            check_utente = 1
        else:
            print("Nome utente sbagliato. Riprova!")
            check_utente = 0


    numero_tentativi = 0
    check_password = 0
    while check_password == 0 and numero_tentativi < 3:
        password = input("Inserisci la password: ")
        numero_tentativi += 1
        check_password = password == "000" # generalizzare seconda condizione

    if numero_tentativi == 3 and check_password == 0:
        print("Tentativi terminati")
    else:
        print("Autenticazione eseguita con successo!")

elif operazione == "2":
    print("Benvenuto nella procedura di registrazione!")
elif operazione == "3":
    print("Arrivederci!")
else:
    print("Scelta non corretta")
    # dare la possibilità di inserire nuova scelta?