import banca

def chiedeCambiaPassword(utente):
    cambio_password = input("Vuoi cambiare la password?\n Digita 1 per effettuare il cambio password\n Digita 2 se vuoi proseguire con la password attuale\n")
    if cambio_password == "1":
        nuova_password = input("Nuova password: ")
        utente.cambiaPassword(nuova_password)
    elif cambio_password != "2":
        print("Scelta non valida.\n")
        chiedeCambiaPassword(utente)
    

