# PyBanking
---
## Indice
- [Coding Rules](#coding-rules)
- [Guida all'utilizzo](#guida-allutilizzo)
- [Struttura dei files](struttura-dei-files)
- [File main.py](file-main)
- [File funzioni.py](file-funzioni)
- [File banca.py](file-banca)
- [File archivio.py](file-archivio)
- [File creazione.py](file-archivio)
- [File manipolazione.py](file-manipolazione)
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

## STRUTTURA DEI FILES
I file presenti sono i seguenti:
- main.py : contiene il codice che descrive l'**interfaccia** utente;
- funzioni.py : contiene alcune funzioni utilizzate nel *main*;
- banca.py: contiene la classe `Utente`, con i relativi metodi;
- archivio.py: contiene il codice che crea una variabile `lista_utenti`, contenente oggetti della classe `Utente` generati randomicamente;
- creazione.py: contiene le funzioni utilizzate in *archivio* per la generazione di liste casuali;
- manipolazione.py: creazione di DataFrame Pandas dedicati contenenti l'elenco dei clienti e il registro dei movimenti.

## File main.py
Il file main.py è spiegato nel dettaglio nel file *spiegazione codice main.md*.

## File funzioni.py
Il file contiene alcune funzioni utilizzate nel *main* che permettono di:

 - chiedere all'utente se desidera cambiare password e in caso affermativo
   modificare la password come richiesto dall'utente

       def  chiedeCambiaPassword(utente):
		    Args:
			    utente (object) : oggetto della classe Utente

 - controllare se il nome e il cognome sono composti solo da lettere e in caso contrario chiedere un nuovo inserimento
   
       def  controlloNome(nome):
	       Args:
		       nome (str) : nome inserito dall'utente
	       Returns:
		       nome (str) : nome aggiornato dall'utente se aveva precedentemento inserito caratteri sbagliati 

 - Controllare se il numero di telefono è composto solo da 10 cifre e in
   caso contrario chiedere un nuovo inserimento
   
       def  controlloNumero(num_telefono)
	       Args:
		       num_telefono (str) : numero di telefono inserito dall'utente
	       Returns:
		       num_telefono (str) : numero di telefono aggiornato dall'utente se aveva precedentemento inserito un formato sbagliato

 - Controlla se l'anno è in un formato corretto e in caso contrario
   chiede un nuovo inserimento
   
       def  controlloAnno(anno):
   	    Args:
   		    anno (str) : anno inserito dall'utente
   	    Returns:
   		    anno (str) : anno aggiornato dall'utente se aveva precedentemento inserito un formato sbagliato

 - Controlla se il mese è in un formato corretto e in caso contrario
   chiede un nuovo inserimento
   
       def  controlloMese(mese):
       Args:
       mese (str) : mese inserito dall'utente
       Returns:
       mese (str) : mese aggiornato dall'utente se aveva precedentemento inserito un formato sbagliato

  

 - Controlla se il giorno è in un formato corretto e in caso contrario
   chiede un nuovo inserimento. Controlla il giorno anche in base all'anno e al mese selezionati.
   
       def  controlloGiorno(giorno,mese,anno):
	       Args:
		       giorno (str) : giorno inserito dall'utente
	       mese (str) : mese inserito dall'utente
		       anno (str) : anno inserito dall'utente
	       Returns:
		       giorno (str) : giorno aggiornato dall'utente se aveva precedentemento inserito un formato sbagliato

## File banca.py

### Caratteristiche  
 - Creazione di account utente con informazioni personali di base 
 - Generazione automatica di password casuali 
 - Operazioni di deposito e prelievo 
 - Gestione del saldo dell'account 
 - Tracciamento e generazione di rapporti delle transazioni

### Codice

#### Funzione generaPassword

		 def  generaPassword(lunghezza):

     
*Genera una password della lunghezza richiesta, prendendo 
	randomicamente caratteri tra lettere, numeri e punteggiatura.*
	
#### Classe Utente
Creazione della **classe Utente** per la gestione degli account utente;

         class  Utente: 	  
        def  __init__(self, nome, cognome, data_nascita, indirizzo, num_telefono, saldo  =  0, registro  =  None, utente  =  0):

*Permette la creazione di oggetti Utenti inserendo nome, cognome, data di nascita, indirizzo e numero di telefono. 
I valori di saldo, registro delle transazioni e codice utente possono essere inseriti nel momento della creazione, altrimenti di default il saldo è nullo, il registro è vuoto e il codice utente è 0.*


	Classe Utente:
    Args:
     	nome (str) : nome utente 
   	 cognome (str) : cognome utente
   	 data_nascita (datetime.date) : data nascita utente
    	 indirizzo (str) : indirizzo utente
   	  num_telefono (int) : numero di telefono utente
    	 saldo (int) : saldo attuale,
	     				default =0
	     registro (matrix) : registro operazioni,
							lista contenente liste del tipo [Id_utente (int), data operazione (datetime), nome operazione(str), operazione (int), saldo (int)],  
							 default = [[0, data creazione conto, "creazione conto", 0, 0]]
		 utente (int) : id utente,
						default = 0

All'interno della classe sono presenti inoltre le definizione di funzioni che permettano la gestione delle credenziali e di alcune operazioni bancarie e  stampa del report contenente le transazioni avvenute. 
In particolare, all'interno della classe Utente, sono state definite **funzioni**, che permettono le seguenti operazioni:


 - *Aggiornare l'oggetto della classe Utente inserendo utente e password.*

		def  creaCredenziali(self, numero_utenti):`
 
   			Args:
 	    	 	numero_utenti (int) : numero utenti già registrati

     

 - *Stampare le credenziali dell'Utente*

		def  stampaCredenziali(self):

 - *Cambiare la password dell'Utente*

	    def  cambiaPassword (self, nuova_password):
   
   			Args:
 	    		nuova_password (str) : password che si vuole inserire

 - *Controllare la password inserita*
		
		def  passwordCorretta(self, password_inserita):

   			Args:
   				password_inserita (str) : password inserita dall'utente
   			Returns:
   				True se la password corrisponde con quella dell'Utente
 				False altrimenti

 - *Aggiornare il saldo depositando la somma richiesta, aggiornare il registro delle operazioni e stampare il messaggio di operazione riuscita*
 
		 def  deposita(self, deposito):

		     Args:
		     		deposito (int) : somma di denaro che si vuole depositare

- *Aggiornare il saldo prelevando la somma richiesta, aggiornare il registro delle operazioni e stampare il messaggio di operazione riuscita*
 
		 def  preleva(self, prelievo):

		     Args:
		     		prelievo (int) : somma di denaro che si vuole prelevare

- *Aggiornare il saldo trasferendo la somma richiesta, aggiornare il registro delle operazioni e stampare il messaggio di operazione riuscita*
 
		 def  trasferisci(self, somma):

		     Args:
		     		somma (int) : somma di denaro che si vuole trasferire

- *Aggiornare il saldo ricevendo la somma richiesta, aggiornare il registro delle operazioni*
 
		 def  ricevi(self, somma):

		     Args:
		     		somma (int) : somma di denaro che si deve ricevere

 - *Stampare il saldo attuale e il report delle transazioni avvenute in
   precedenza*

		def  stampaReport(self):

## File archivio.py

Sono stati creati alcuni utenti, con l'esecuzione di varie operazioni bancarie come depositi, prelievi, trasferimenti e generazione di rapporti delle transazioni e sono stati inseriti all'interno di una lista, chiamata `lista_utenti`.

## File creazione.py

## File manipolazione.py 

Al fine di agevolare l'analisi dei dati immagazzinati nella classe utente si è proseguito alla creazione di Dataframe Pandas dedicati contenenti l'elenco dei clienti e il registro dei movimenti.
La creazione del registro dei movimenti ha necessitato, partendo dalla lista_utenti precedentemente definita, la creazione di una lista di dataframes contenente le informazioni racchiuse nel registro. Successivamente definendo la funzione concat_dataframes si è giunti al df_operazioni d'interesse nel quale in ogni riga descrive una singola operazione registrata.


>    def concat_dataframes(lista_df):
>        Concatena una lista di df pandas in un unico nuovo df
>    
>    Args:
>        lista_df= lista contente per ogni elemento un df
>    
>    Return:
>        concat_df = pandas df


Per ottenere l'elenco dei clienti è stata poi definita la funzione crea_df_utente() la quale individuando dalla lista_utenti le informazioni d'interesse e raccogliendole lungo liste vuote raccolte all'interno di un dizionaraio dedicato permette la restituzione di un dataframes pandas contenente informazione personali degli utenti.


>    def crea_df_utente():
>   '''
>    Crea un df pandas ove ogni riga conterrà le informaioni
>    relative ad un un singolo Utente 
>    
>    Args:
>        None
>
>    Returns:
>        df_utenti : pandas dataframe
>
>    '''


I due dataframe creati sono infine stati uniti tramite operazione di merge lungo la variabile comune indicante l' id utente in un terzo dataframe pandas il quale permette di associare ogni operazione effettuata ai dati personali del soggetto interessato.

Dopo una breve manipolazione del nuovo df, si è salvato un csv, poi riutilizzabile in operazione future in altri ambienti.
