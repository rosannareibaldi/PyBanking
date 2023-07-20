import banca
import sys
import time

def chiedeCambiaPassword(utente):
    """ Chiede all'utente se desidera cambiare password e in caso affermativo modifica la password come richiesto dall'utente
    Args:
        utente (object) : oggetto della classe Utente
    """
    cambio_password = input("Vuoi cambiare la password?\n Digita 1 per effettuare il cambio password\n Digita 2 se vuoi proseguire con la password attuale\n")
    if cambio_password == "1":
        nuova_password = input("Nuova password: ")
        utente.cambiaPassword(nuova_password)
    elif cambio_password != "2":
        print("Scelta non valida.\n")
        chiedeCambiaPassword(utente)

def controlloNome(nome):
    """ Controlla se il nome è composto solo da lettere e in caso contrario chiede un nuovo inserimento
    Args:
        nome (str) : nome inserito dall'utente
    Returns:
        nome (str) : nome aggiornato dall'utente se aveva precedentemento inserito caratteri sbagliati
    """
    if not nome.isalpha():
        print("Formato non corretto. Inserire solo lettere.\n")
        nome = input ("Inserisci il tuo nome: ")
        controlloNome(nome)
    return nome

def controlloCognome(cognome):
    """ Controlla se il cognome è composto solo da lettere e in caso contrario chiede un nuovo inserimento
    Args:
        cognome (str) : cognome inserito dall'utente
    Returns:
        cognome (str) : cognome aggiornato dall'utente se aveva precedentemento inserito caratteri sbagliati
    """
    if not cognome.isalpha():
        print("Formato non corretto. Inserire solo lettere.\n")
        cognome = input ("Inserisci il tuo cognome: ")
        controlloCognome(cognome)
    return cognome

def controlloNumero(num_telefono):
    """ Controlla se il numero di telefono è composto solo da 10 cifre e in caso contrario chiede un nuovo inserimento
    Args:
        num_telefono (str) : numero di telefono inserito dall'utente
    Returns:
        num_telefono (str) : numero di telefono aggiornato dall'utente se aveva precedentemento inserito un formato sbagliato
    """
    if not num_telefono.isdigit() or len(num_telefono)!=10:
        print("Formato non corretto. Inserire 10 cifre.\n")
        num_telefono = input ("Inserisci il tuo numero di telefono: ")
        controlloNumero(num_telefono)
    return num_telefono

def controlloAnno(anno):
    """ Controlla se l'anno è in un formato corretto e in caso contrario chiede un nuovo inserimento
    Args:
        anno (str) : anno inserito dall'utente
    Returns:
        anno (str) : anno aggiornato dall'utente se aveva precedentemento inserito un formato sbagliato
    """
    if not anno.isdigit() or len(anno)!=4 or int(anno)>2023 or int(anno)<0:
        print("Formato non corretto. Inserire l'anno nel formato 1990.\n")
        anno = input ("Inserisci il tuo anno di nascita: ")
        controlloAnno(anno)
    return anno

def controlloMese(mese):
    """ Controlla se il mese è in un formato corretto e in caso contrario chiede un nuovo inserimento
    Args:
        mese (str) : mese inserito dall'utente
    Returns:
        mese (str) : mese aggiornato dall'utente se aveva precedentemento inserito un formato sbagliato
    """
    if not mese.isdigit() or int(mese)>12 or int(mese)<1:
        print("Formato non corretto. Inserire il mese nel formato 1,2,3, ... .\n")
        mese = input ("Inserisci il tuo mese di nascita: ")
        controlloMese(mese)
    return mese

def controlloGiorno(giorno,mese,anno):
    """ Controlla se il giorno è in un formato corretto e in caso contrario chiede un nuovo inserimento. 
        Controlla il giorno anche in base all'anno e al mese selezionati.
    Args:
        giorno (str) : giorno inserito dall'utente
        mese (str) : mese inserito dall'utente
        anno (str) : anno inserito dall'utente
    Returns:
        giorno (str) : giorno aggiornato dall'utente se aveva precedentemento inserito un formato sbagliato
    """
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
    return giorno


def stampa_simulata(testo):
    for carattere in testo:
        sys.stdout.write(carattere)
        sys.stdout.flush()
        time.sleep(0.02)  # Puoi regolare il tempo di pausa tra i caratteri qui
    print()  # Andare a capo dopo aver stampato tutto il testo


