# PyBanking
---
## Coding rules
### Indentazione e formattazione
Inserire righe vuote:

 - In caso di due blocchi di codice differenti verranno lasciate tre righe vuote tra la fine del primo blocco ed l'eventuale commento posto prima del blocco successivo;
 - All'interno dello stesso blocco di codice, a discrezione dell'utente, potrà essere inserita una riga vuota al fine di migliorare la leggibilità delle istruzioni per il controllo di flusso.

Durante l'intero progetto verrà  rispettata l'identazione python tramite singola tabulazione. Inoltre, verranno utilizzati spazi bianchi tra gli operatori e dopo
le virgole per separare i parametri nelle funzioni.

### Nomenclatura

 - nomi variabili: snake case;
 - nomi funzioni: camel case;
 - costanti: in maiuscolo;
 - nomi classi: iniziale maiuscola.

### Commenti

 - Subito dopo la definizione di una funzione, verrà inserita una docstring in Google style, così come esemplificato:
>        def standardize(column):
>      """Standardize the values in a column.
>    
>      Args:
>        column (pandas Series): The data to standardize.
>    
>      Returns:
>        pandas Series: the values as z-scores
>      """
>      z_score = (column - column.mean()) / column.std()
>      return z_score
>      print(standardize.__doc__)

 - Prima di ogni blocco di codice verrà inserito un commento che ne spieghi il funzionamento;
 - All'interno dei blocchi l'inserimento dei commenti è a discrezione dell'utente.

### Organizzazione dei files

 - Funzioni e classi verranno definite in files separati ed eventualmente raggruppate tra loro, a discrezione dell'utente


## **GUIDA ALL'UTILIZZO**

Inizializzando il programma verrà stampato il messaggio di benvenuto: 
"Ciao! Benvenuti nella banca PyBanking" e conseguentemente una prima finestra operativa
che consente all'utente di eseguire, tramite input tre differenti interazioni con il programma.
Digitando 1 si proseguirà all'accesso tramite autenticazione, digitando 2 si permetterà ai nuovi utenti di effettuare la registrazione, digitando 3 si effettuerà il log out della sessione.L'inserimento di valori non consentiti genererà un messagio di errore.

La registrazione(attivata dalla digitazione:2) richiederà al nuovo utilizzatore di inserire alcuni suoi dati personali: il 'Nome', il 'Cognome', l' 'Indirizzo', il 'Numero di telefono',
e la data di nascita individuando speratamente 'Giorno', 'Mese', 'Anno'. L'inserimento di tali valori, se eseguito correttamente permetterà all'utente di registrarsi all'interno del registro della banca, e di ricevere il proprio 'Utente' e la propria 'Password' poi necessari ad effettuare l'identificazione e l'accesso al terminale. Successivamente l'utente sarà ricondotto automaticamente alla finestra operativa principale.

Eseguendo l'accesso (attivato dalla digitazione:1) dall'interno del terminale il programma richiederà di inserire il proprio 'Utente' e la 'Password' con l'opzione di tornare alla schermata principale digitando 'INDIETRO'. Inserito un 'Utente' valido, l'utilizzatore avrà tre tentativi per per inserire la 'Password' corretta, nel caso in cui non si inserisse la password corretta l'utente verrebbe disabilitato. In caso l'Utente' inserito non fosse valido verrà generato un messaggio di errore e verrà richiesto nuovamente di inserire un 'Utente valido'. 
L'inserimento di credenziali valide permetterà al programma di aprire un ulteriore menù, il quale tramite input permetterà all'utente di effettuare diversi tipi di operazioni: il 'deposito' (attivabile digitando: 1), il 'prelievo (attivabile digitando: 2)', il 'trasferimento' (attivabile digitando: 3), la 'stampa report'(attivabile digitando: 4) ed 'esci'(attivabile digitando: 5) che permetterà di interrompere la sessione.

L'operazione 'deposito', richiederà di inserire tramite input la somma numerica che si vuole depositare, l'inserimento di valori errati ritornerà un messaggio di errore, contrariamente, inserita una cifra valida il programma aggiornerà il 'saldo' dell'utente e stamperà un messaggio contenente la notizia di operazione avvenuta e il saldo post operazione.

L'operazione 'prelievo', similmente, richiederà di inserire tramite input la somma numerica che si vuole prelevare, l'inserimento di valori errati ritornerà un messaggio di errore, come la richiesta di prelevare una cifra maggiore al saldo disponibile al momento del prelievo da parte dell'utente. Contrariamente, inserita una cifra valida il programma aggiornerà il 'saldo' dell'utente e stamperà un messaggio contenente la notizia di operazione avvenuta e il saldo post operazione.

L'operazione 'trasferimento', permetterà, a condizione che venga inserito un 'Utente' di un 
altro soggetto esistente all'interno del sistema della banca, di trasferire una quantità di denaro in un conto differente. Successivamente il programma aggiornerà entrambi i saldi interessati e stamperà all'intestatario un messaggio contenente la notizia di operazione avvenuta e il saldo post operazione.

L'operazione 'stampa report', permetterà all'utente di visualizzare un report contenente alcune informazioni riguardanti il proprio conto come: il proprio saldo, il saldo medio per mese e la sua evoluzione storica, la lista di operazioni effettuate.


Durante l'inizializzazione di una delle cinque operazioni sovraelencate sarà possibile digitando 'menu' al posto dell'input richiesto di tornare al menù operativo dal quale si potrà inizializzare una nuova operazione. Similmente succederà se portata a termine una singola operazione.
