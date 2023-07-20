import random
import datetime

def generaNomiPropri(num_nomi):
    """
    Genera una lista di nomi propri casuali.

    Args:
        num_nomi (int): Il numero di nomi propri da generare.

    Returns:
        list: Lista di nomi propri casuali.
    """
    nomi_propri = []
    for _ in range(num_nomi):
        nome = random.choice([
            "Mario", "Luca", "Francesca", "Giulia", "Andrea", "Alessia", "Matteo", "Sara", "Lorenzo", "Elisa",
            "Gabriele", "Valentina", "Davide", "Chiara", "Simone", "Greta", "Nicola", "Alice", "Marco", "Martina",
            "Giovanni", "Federica", "Riccardo", "Emma", "Samuele", "Elena", "Tommaso", "Anna", "Alessandro", "Laura"
            # Aggiungi altri nomi propri desiderati qui
        ])
        nomi_propri.append(nome)
    return nomi_propri


def generaCognomi(num_cognomi):
    """
    Genera una lista di cognomi casuali.

    Args:
        num_cognomi (int): Il numero di cognomi da generare.

    Returns:
        list: Lista di cognomi casuali.
    """
    cognomi = []
    for _ in range(num_cognomi):
        cognome = random.choice([
            "Rossi", "Russo", "Ferrari", "Esposito", "Bianchi", "Romano", "Colombo", "Ricci", "Marini", "Galli",
            "Conti", "Costa", "De Luca", "Mancini", "Rizzo", "Lombardi", "Moretti", "Barbieri", "Fontana", "Santoro",
            "Mariani", "Rinaldi", "Caruso", "Ferraro", "Galli", "Martini", "Leone", "Greco", "Serra", "De Santis"
            # Aggiungi altri cognomi desiderati qui
        ])
        cognomi.append(cognome)
    return cognomi


def generaDateNascita(num_date):
    """
    Genera una lista di date di nascita casuali.

    Args:
        num_date (int): Il numero di date di nascita da generare.

    Returns:
        list: Lista di date di nascita casuali.
    """
    date_nascita = []
    for _ in range(num_date):
        anno = random.randint(1950, 2005)
        mese = random.randint(1, 12)
        giorno = random.randint(1, 28)
        data = datetime.date(anno, mese, giorno)
        date_nascita.append(data)
    return date_nascita



def generaIndirizzi(num_indirizzi):
    """
    Genera una lista di indirizzi casuali.

    Args:
        num_indirizzi (int): Il numero di indirizzi da generare.

    Returns:
        list: Lista di indirizzi casuali.
    """
    indirizzi = []
    for _ in range(num_indirizzi):
        via = random.choice([
            "Via Roma", "Via Milano", "Via Napoli", "Via Venezia", "Via Firenze", "Via Bologna", "Via Torino",
            "Via Genova", "Via Verona", "Via Palermo", "Via Padova", "Via Bari", "Via Trieste", "Via Catania",
            "Via Perugia", "Via Pisa", "Via Modena", "Via Siena", "Via Livorno", "Via Ancona", "Via Lecce",
            "Via Ravenna", "Via Matera", "Via Salerno", "Via Siracusa", "Via Cagliari", "Via Pavia", "Via Varese",
            "Via Treviso", "Via Udine"
            # Aggiungi altri indirizzi desiderati qui
        ])
        numero = random.randint(1, 100)
        indirizzo = f"{via}, {numero}"
        indirizzi.append(indirizzo)
    return indirizzi


def generaNumeriTelefono(num_numeri):
    """
    Genera una lista di numeri di cellulare casuali.

    Args:
        num_numeri (int): Il numero di numeri di cellulare da generare.

    Returns:
        list: Lista di numeri di cellulare casuali.
    """
    numeri_cellulare = []
    for _ in range(num_numeri):
        numero = "".join(random.choice("0123456789") for _ in range(10))
        numeri_cellulare.append(numero)
    return numeri_cellulare

def generaSaldi(num_numeri):
    """
    Genera una lista di numeri casuali.

    Args:
        num_numeri (int): Il numero di numeri casuali da generare.
        min_val (int): Il valore minimo incluso nel range.
        max_val (int): Il valore massimo escluso dal range.

    Returns:
        list: Lista di numeri casuali.
    """
    numeri_casuali = []
    for _ in range(num_numeri):
        numero = random.randint(0, 60000)
        numeri_casuali.append(numero)
    return numeri_casuali

def generaRegistro(data_precedente, saldo):
    """
    Genera una lista contente gli elementi di un'operazione, in maniera casuale

    Args:
        data_precedente (date) : data dell'operazione precedente 

    Returns:
        registro_operazione (list) : lista contente [0, data operazione, descrizione operazione, somma spostata, saldo aggiornato]]
        """
    giorni = random.randint(1,30)
    data_operazione = data_precedente + datetime.timedelta(days=giorni)
    lista_operazioni = ["prelievo", "deposito", "trasferimento", "ricevimento"]
    operazione = random.choice(lista_operazioni)

    if operazione == "prelievo" or operazione == "trasferimento":
        somma = random.randint(0,saldo)
        saldo -= somma   
        registro_operazione = [0, data_operazione, operazione, -somma, saldo]
    else:
        somma = random.randint(1,10000)
        saldo += somma 
        registro_operazione = [0, data_operazione, operazione, somma, saldo]  

    return registro_operazione






