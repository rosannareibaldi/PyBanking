Il codice inizia caricando i files esterni necessari alla corretta esecuzione del programma, ovvero `datetime`, `getpass`, `time`, `banca`, `funzioni` e `lista_utenti` da `archivio`.

Dopo aver stampato il messaggio di benvenuto, viene visualizzata la finestra operativa che consente all'utente di scegliere l'operazione da effettuare, digitando:

 - *1* per eseguire l'accesso;
 - *2* per effettuare la registrazione;
 - *3* per uscire.

Questa finestra operativa viene stampata al completamento di ogni operazione, a meno che l'utente non chieda di uscire dal programma digitando *3*. Ciò è possibile strutturando il codice come segue:

    while  operazione  !=  "3":
	    if  operazione  ==  "1":
		    ...
	    elif  operazione  ==  "2":
		    ...
	    else:
		    funzioni.stampa_simulata("Scelta non corretta\n")
		    operazione  =  input("Digita 1 se vuoi eseguire l'accesso \nDigita 2 se vuoi effettuare \
		    la registrazione \nDigita 3 se vuoi uscire \n")
    
In questo modo, inoltre, quando l'utente inserisce un valore non consentito per la variabile `operazione`, il programma lo segnala e permette di inserire un nuovo input.

Quando l'utente scegliere di eseguire l'accesso, ovvero  `operazione  =  "1"`, il programma chiede l'inserimento del codice utente fino a quando non viene inserito il codice di un utente già registrato; inoltre, digitando la parola *INDIETRO* l'utente ha la possibilità di ritornare alla schermata principale. A tal fine viene utilizzata la variabile di controllo `check_utente`, inizializzata a 0: tale variabile assumerà valore 1 se l'utente esprime la volontà di ritornare indietro oppure se il codice utente inserito è già presente nell'archivio della banca; diversamente tale variabile rimarrà uguale a 0 ed il programma continuerà a richiedere l'inserimento di un codice utente.

    check_utente  =  0
    while  check_utente  ==  0:
	    utente  =  input("Inserisci il codice utente oppure digita INDIETRO per tornare \
	alla pagina principale: ")
		if  utente.lower() ==  "indietro":
			check_utente  =  1
			operazione  =  input("Digita 1 se vuoi eseguire l'accesso \nDigita 2 se vuoi \
			effettuare la registrazione \nDigita 3 se vuoi uscire \n")
		else:
			...

Se l'utente esprime la volontà di ritornare indietro, ovvero `utente.lower() == "indietro"`, il programma stampa nuovamente la finestra principale. Diversamente, il programma verifica se il codice utente inserito è presente in archivio: a tal fine viene utilizzata la variabile di controllo `utente_trovato`, inizializzata a 0, che varrà 1 nel momento in cui il codice utente inserito è presente nell'archivio della banca. Per effettuare tale verifica, si procede come segue:

    utente_trovato  =  0
    for  i  in  range(len(lista_utenti)):
	    if  iutente.isdigit() and  int(utente) ==  lista_utenti[i].utente:
		    utente_trovato  =  1
			funzioni.stampa_simulata("Codice utente esistente.\n")
			check_utente  =  1
			utente_attuale  =  lista_utenti[i]
			break
			
Se la verifica va a buon fine, ovvero `utente_trovato = 1`, il codice utente viene memorizzato in `utente_attuale`. In caso contrario, ovvero `utente_trovato = 0`, è possibile inserire un nuovo codice utente oppure tornare indietro per effettuare la registrazione:

    if  utente_trovato  ==  0:
    funzioni.stampa_simulata("Codice utente non presente nel registro. Riprova oppure torna indietro per \
    registrarti!")
    check_utente  =  0

In definitiva, il `while` su `check_utente` termina quando l'utente sceglie di tornare indietro oppure inserisce un codice utente esistente in archivio.
Verificato il codice utente il programma proseguirà con la richiesta e la verifica della password, utilizzando due variabili `numero_tentativi` e `check_password`: la prima conta il numero di tentativi effettuati, mentre la seconda è una variabile di controllo relativa alla correttezza della password. Il programma permette l'inserimento di password non corretta per al massimo 3 tentativi, al termine dei quali il programma si arresta. L'inserimento della password viene interrotto nel momento in cui si inserisci la password corretta, ovvero `check_password = "1"`.

Se la procedura di autenticazione va a buon fine, viene stampato il saldo attuale per poi procedere alla scelta dell'operazione da effettuare:

 - *1* per il deposito;
 - *2* per il prelievo;
 - *3* per il trasferimento di denaro;
 - *4* per la stampa del report;
 - *5* per uscire dal programma.
 
Per le operazioni di *deposito*, *prelievo* e *trasferimento di denaro* il programma continua a richiedere l'inserimento di un valore per la quantità di denaro da depositare, prelevare o trasferire finché questo non sia un valore valido oppure, nel caso di prelievo e trasferimento di denaro, non sia inferiore al saldo disponibile: si utilizza a tal fine la variabile di controllo `inserimento_corretto`, inizializzata a 0, che varrà 1 solo nel caso di valore valido. 
Inoltre per l'operazione di trasferimento il programma continua a richiedere l'inserimento del codice utente del destinatario fino a quando non si inserisce il codice di un utente presente nell'archivio della banca: solo in tal caso viene richiesto l'importo da trasferire, verificandone la correttezza.
Ciascuna delle tre operazioni precedenti comporta l'aggiornamento del saldo.
Per tutte e tre le operazioni, in qualsiasi momento, l'utente ha la possibilità di ritornare al menù precedente digitando *MENU*.

Quando l'utente sceglie la procedura di registrazione, ovvero `operazione = "2"`, vengono richieste alcune informazioni, verificandone la correttezza: 
 - nome,
 - cognome,
 - anno di nascita nel formato *AAAA*,
 -  mese e giorno di nascita senza digitare lo zero iniziale nel caso di una singola cifra,
 - indirizzo,
 - provincia,
 - numero di telefono, nel formato a 10 cifre.

Vengono così create le credenziali e l'utente viene registrato nell'archivio della banca. Al termine della procedura di registrazione, viene fornita all'utente la possibilità di effettuare il cambio password e viene visualizzata la pagina operativa principale per effettuare la scelta dell'operazione da effettuare.
 
