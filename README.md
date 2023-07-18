# PyBanking
---
## Coding rules
### Indentazione e formattazione
Inserire righe vuote:

 - in caso di due blocchi di codice differenti verranno lasciate tre righe vuote tra la fine del primo blocco ed il commento posto prima del blocco successivo;
 - all'interno dello stesso blocco di codice, a discrezione dell'utente, verrà inserita una riga vuota al fine di migliorare la leggibilità delle istruzioni per il controllo di flusso.

Indentazione standard di Python.

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

 - Prima di ogni blocco di codice inserire un commento che ne spieghi il funzionamento;
 - All'interno dei blocchi l'inserimento dei commenti è a discrezione dell'utente.
