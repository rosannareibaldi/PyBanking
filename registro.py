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
                 registro = [[datetime.datetime.now(), "creazione conto", 0, 0]]):
        """Classe Utente:
        Args:
            nome (str) : nome utente
            cognome (str) : cognome utente
            data_nascita (datetime.date) : data nascita utente
            indirizzo (str) : indirizzo utente
            num_telefono (int) : numero di telefono utente
            saldo (int) : saldo attuale, 
                            default =0
            registro (list) : registro operazioni, 
                            lista contenente liste del tipo [data operazione (datetime), nome operazione(str), operazione (int), saldo (int)], 
                            default = [[data creazione conto, "creazione conto", 0, 0]]
            """
        self.nome = nome
        self.cognome = cognome
        self.data_nascita = data_nascita
        self.indirizzo = indirizzo
        self.num_telefono = num_telefono
        self.saldo = saldo
        self.registro = registro
    
    def creaCredenziali(self,numero_utenti):
        """ Aggiorna l'oggetto della classe Utente inserendo utente e password
        Args:
            numero_utenti (int) : numero utenti già registrati 
        """
        self.utente = numero_utenti + 1
        self.__password = generaPassword(8)
        print(f"Registrato!\n Utente: {self.utente}\n Password: {self.__password}")
    
    def deposita(self, deposito):
        """
        Aggiorna il saldo depositando la somma richiesta, aggiorna il registro delle operazioni 
        e stampa il messaggio di operazione riuscita

        Args:
            deposito (int) : somma di denaro che si vuole depositare
        """
        self.saldo += deposito
        self.registro.append([datetime.datetime.now(), "deposito", deposito, self.saldo])
        print(f"Operazione riuscita! Saldo attuale: {self.saldo}€\n")

    def preleva(self, prelievo):
        """
        Aggiorna il saldo prelevando la somma richiesta e aggiorna il registro delle operazioni
        e stampa il messaggio di operazione riuscita

        Args:
            prelievo (int) : somma di denaro che si vuole prelevare
        """
        self.saldo -= prelievo
        self.registro.append([datetime.datetime.now(), "prelievo", - prelievo, self.saldo])
        print(f"Operazione riuscita! Saldo attuale: {self.saldo}€\n")

    def stampaReport(self):
        print("OPERAZIONI EFFETTUATE:\n")
        for riga in self.registro:
            data_str = riga[0].strftime("%d/%m/%Y")
            print(f"Data: {data_str}, Operazione: {riga[1]} di {riga[2]}€, Saldo: {riga[3]} \n")

data_nascita1 = datetime.date(1998, 12, 2)

utente1 = Utente("Lucia", "Ferrari", data_nascita1, "via blabla", 3323458192 )
utente1.creaCredenziali(0)
utente1.deposita(1000)
utente1.preleva(50)
utente1.stampaReport()
#print(utente1.registro)





