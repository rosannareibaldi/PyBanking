import getpass
import random
import string

def generaPassword(lunghezza):
    """ Genera una password della lunghezza richiesta, prendendo randomicamente caratteri tra lettere, numeri e punteggiatura.

    Args:
        lunghezza: lunghezza della password

    Returns:
        password: password randomica
    """
    caratteri = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(caratteri) for _ in range(lunghezza))
    return password

class Utente:
    def __init__(self, nome, cognome, data_nascita, indirizzo, num_telefono):
        self.nome = nome
        self.cognome = cognome
        self.data_nascita = data_nascita
        self.indirizzo = indirizzo
        self.num_telefono = num_telefono
        self.saldo = 0
    
    def creaCredenziali(self,numero_utenti):
        """ Crea le credenziali utente e password.
        Args:
            numero_utenti: numero utenti già registrati
            
        Aggiorna l'oggetto della classe Utente inserendo utente e password
        """
        self.utente = numero_utenti + 1
        self.__password = generaPassword(8)
    
    def deposita(self,deposito):
        self.saldo += deposito

    def preleva(self,prelievo):
        self.saldo -= prelievo


 #   def trasferisci():

 #   def stampaReport():

