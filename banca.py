import random
import string
import datetime

def generaPassword(lunghezza):
    """ Genera una password della lunghezza richiesta, prendendo randomicamente caratteri tra lettere, numeri e punteggiatura.

    Args:
        lunghezza (int) : lunghezza della password

    Returns:
        password (str) : password randomica
    """
    caratteri = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(caratteri) for _ in range(lunghezza))
    return password


class Utente:
    def __init__(self, nome, cognome, data_nascita, indirizzo, num_telefono, saldo = 0, \
                 registro = None, utente = 0):
        """Classe Utente:
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
            """
        if registro is None:
            registro = [[0, datetime.datetime.now(), "creazione conto", 0, 0]]
        self.nome = nome
        self.cognome = cognome
        self.data_nascita = data_nascita
        self.indirizzo = indirizzo
        self.num_telefono = num_telefono
        self.saldo = saldo
        self.registro = registro
        self.utente = utente
    
    def creaCredenziali(self,numero_utenti):
        """ Aggiorna l'oggetto della classe Utente inserendo utente e password
        Args:
            numero_utenti (int) : numero utenti già registrati 
        """
        self.utente = numero_utenti + 1
        for i in range(len(self.registro)):
            self.registro[i][0] = self.utente
        self.__password = generaPassword(8)
    
    def stampaCredenziali(self):
        """ Stampa le credenziali dell'Utente 
        """
        print(f"Utente: {self.utente}\n Password: {self.__password}\n")

    def cambiaPassword (self, nuova_password):
        """ Cambia la password dell'Utente
        Args:
            nuova_password (str) : password che si vuole inserire
            """
        self.__password = nuova_password
    
    def passwordCorretta(self, password_inserita):
        """ Controllo password
        Args:
            password_inserita (str) : password inserita dall'utente
        Returns:
            True se la password corrisponde con quella dell'Utente
            False altrimenti
        """
        if self.__password == password_inserita:
            return True
        else:
            return False
    
    def deposita(self, deposito):
        """
        Aggiorna il saldo depositando la somma richiesta, aggiorna il registro delle operazioni 
        e stampa il messaggio di operazione riuscita

        Args:
            deposito (int) : somma di denaro che si vuole depositare
        """
        self.saldo += deposito
        self.registro.append([self.utente, datetime.datetime.now(), "deposito", deposito, self.saldo])
        print(f"Operazione riuscita! Saldo attuale: {self.saldo}€\n")
        
    def preleva(self, prelievo):
        """
        Aggiorna il saldo prelevando la somma richiesta, aggiorna il registro delle operazioni
        e stampa il messaggio di operazione riuscita

        Args:
            prelievo (int) : somma di denaro che si vuole prelevare
        """
        self.saldo -= prelievo
        self.registro.append([self.utente, datetime.datetime.now(), "prelievo", - prelievo, self.saldo])
        print(f"Operazione riuscita! Saldo attuale: {self.saldo}€\n")

    def ricevi(self, somma):
        """
        Aggiorna il saldo ricevendo la somma trasferita, aggiorna il registro delle operazioni 

        Args:
            somma (int) : somma di denaro che si deve ricevere
        """
        self.saldo += somma
        self.registro.append([self.utente, datetime.datetime.now(), "ricevimento", somma, self.saldo])
    
    def trasferisci(self, somma):
        """
        Aggiorna il saldo prelevando la somma richiesta, aggiorna il registro delle operazioni
        e stampa il messaggio di operazione riuscita

        Args:
            somma (int) : somma di denaro che si vuole trasferire
        """
        self.saldo -= somma
        self.registro.append([self.utente, datetime.datetime.now(), "trasferimento", - somma, self.saldo])
        print(f"Operazione riuscita! Saldo attuale: {self.saldo}€\n")

    def stampaReport(self):
        """ Stampa il saldo attuale e il report delle transazioni avvenute in precedenza
        """
        print(f"SALDO ATTUALE: {self.saldo}€\n")
        print("OPERAZIONI EFFETTUATE:\n")
        for riga in self.registro:
            data_str = riga[1].strftime("%d/%m/%Y")
            print(f"Data: {data_str}, Operazione: {riga[2]} di {riga[3]}€, Saldo: {riga[4]}€ \n")











