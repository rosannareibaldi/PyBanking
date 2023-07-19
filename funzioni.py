import banca

def chiedeCambiaPassword(utente):
    cambio_password = input("Vuoi cambiare la password?\n Digita 1 per effettuare il cambio password\n Digita 2 se vuoi proseguire con la password attuale\n")
    if cambio_password == "1":
        nuova_password = input("Nuova password: ")
        utente.cambiaPassword(nuova_password)
    elif cambio_password != "2":
        print("Scelta non valida.\n")
        chiedeCambiaPassword(utente)

def controlloNome(nome):
    if not nome.isalpha():
        print("Formato non corretto. Inserire solo lettere.\n")
        num_telefono = input ("Inserisci il tuo nome: ")
        controlloNome(nome)

def controlloCognome(cognome):
    if not cognome.isalpha():
        print("Formato non corretto. Inserire solo lettere.\n")
        num_telefono = input ("Inserisci il tuo cognome: ")
        controlloCognome(cognome)

def controlloNumero(num_telefono):
    if not num_telefono.isdigit() or len(num_telefono)!=10:
        print("Formato non corretto. Inserire 10 cifre.\n")
        num_telefono = input ("Inserisci il tuo numero di telefono: ")
        controlloNumero(num_telefono)

def controlloAnno(anno):
    if not anno.isdigit() or len(anno)!=4 or int(anno)>2023 or int(anno)<0:
        print("Formato non corretto. Inserire l'anno nel formato 1990.\n")
        anno = input ("Inserisci il tuo anno di nascita: ")
        controlloAnno(anno)

def controlloMese(mese):
    if not mese.isdigit() or int(mese)>12 or int(mese)<1:
        print("Formato non corretto. Inserire il mese nel formato 1,2,3, ... .\n")
        mese = input ("Inserisci il tuo mese di nascita: ")
        controlloMese(mese)

def controlloGiorno(giorno,mese,anno):
    if not giorno.isdigit() or int(giorno)<0:
        print("Formato non corretto. Inserire il giorno nel formato 1,2,3, ... .\n")
        giorno = input ("Inserisci il tuo giorno di nascita: ")
        controlloGiorno(giorno,mese,anno)
    elif int(mese) in (1,3,5,7,8,10,12):
        if int(giorno)>31:
            print("Formato non corretto. Il mese ha 31 giorni. Inserire il giorno nel formato 1,2,3, ... .\n")
            giorno = input ("Inserisci il tuo giorno di nascita: ")
            controlloGiorno(giorno,mese,anno)
    elif int(mese) in (4,6,9,11):
        if int(giorno)>30:
            print("Formato non corretto. Il mese ha 30 giorni. Inserire il giorno nel formato 1,2,3, ... .\n")
            giorno = input ("Inserisci il tuo giorno di nascita: ")
            controlloGiorno(giorno,mese,anno)
    elif int(mese)==2:
        if int(anno)%4==0 and int(giorno)>29:
            print(f"Formato non corretto. Febbraio aveva 29 giorni nel {anno}. Inserire il giorno nel formato 1,2,3, ... .\n")
            giorno = input ("Inserisci il tuo giorno di nascita: ")
            controlloGiorno(giorno,mese,anno)   
        elif int(giorno)>28:
            print(f"Formato non corretto. Febbraio aveva 28 giorni nel {anno}. Inserire il giorno nel formato 1,2,3, ... .\n")
            giorno = input ("Inserisci il tuo giorno di nascita: ")
            controlloGiorno(giorno,mese,anno)       
