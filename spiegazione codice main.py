Il codice inizia caricando i file esterni necessari alla corretta esecuzione del programma, tramite le seguenti istruzioni:

    import  datetime
    import  banca
    import  funzioni
    from  archivio  import  lista_utenti

Inizialmente viene stampato il messaggio di benvenuto

    print("Ciao! Benvenuto nella banca PyBanking!")
    
e successivamente viene visualizzata la finestra operativa che consente all'utente di scegliere l'operazione da effettuare

    operazione  =  input("Digita 1 se vuoi eseguire l'accesso \nDigita 2 se vuoi effettuare la registrazione \nDigita 3 se vuoi uscire \n")

Questa finestra operativa viene stampata al completamento di ogni operazione, a meno che l'utente non chieda di uscire dal programma digitando 3. Ciò è possibile inserendo tutte le istruzioni all'interno del ciclo

    while  operazione  !=  "3":
