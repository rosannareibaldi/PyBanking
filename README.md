# PyBanking
---
## Coding rules
### Indentazione e formattazione
Inserire righe vuote:

 - In caso di due blocchi di codice differenti verranno lasciate tre righe vuote tra la fine del primo blocco ed l'eventuale commento posto prima del blocco successivo;
 - All'interno dello stesso blocco di codice, a discrezione dell'utente, potrà essere inserita una riga vuota al fine di migliorare la leggibilità delle istruzioni per il controllo di flusso.

Durante l'intero rpogetto verrà  rispettata l'identazione python tramite singola tabulazione.

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
