# Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione. L'operazione può procedere solo se la condizione A è vera o se 
# entrambe le condizioni B e C sono vere. La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.

def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA is True or (conditionB and conditionC) is True:
        return 'Operazione permessa'
    else:
        return 'Operazione negata'

print(check_combination(True, False, True))
print(check_combination(False, True, False))

#Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.

def sum_above_threshold(numbers: list[int], x:int) -> int:
    lista = []
    for num in numbers:
        if x <= num:
            lista.append(num)
            return sum(lista)

	
print(sum_above_threshold([15, 5, 25], 20))

# Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
# a) 1, 2, 3, 4, 5, 6, 7
# b) 3, 8, 13, 18, 23
# c) 20, 14, 8, 2, -4, -10
# d) 19, 27, 35, 43, 51

def print_seq(): 
    
    print("Sequenza a):")
    for num in range(1,8):
        print(num)

    print("Sequenza b):")
    for num in range(3,24,5):
        print(num)

    print("Sequenza c):")
    for num in range(20,-11,-6):
        print(num)

    print("Sequenza d):")
    for num in range(19,52,8):
        print(num)
    
print_seq()
#Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.
def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    new_dict = {}
    for key,value in prodotti.items():
        if value > 20:
            new_dict[key] = value - (value * 0.1)
    return new_dict

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0})) 

# Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
# - se x è pari, deve essere diviso per 2;
# - se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1.
def transform(x: int) -> int:
    if x % 2 == 0:
        x /= 2
    else:
        x = (x * 3) -1
    return int(x)
print(transform(5))
print(transform(-10))

#Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    dict3 = dict1.copy()
    for key, value in dict2.items():
        if key in dict3:
            dict3[key] += value
        else:
            dict3[key] = value
    return dict3

print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))

# Progettare un sistema di videonoleggio con i seguenti requisiti:

# 1. Classe Movie:

# Attributi:

# movie_id: str - Identificatore di un film.
# title: str - Titolo del film.
# director: str - Regista del film.
# is_rented: boolean - Booleano che indica se il film è noleggiato o meno.
# Metodi:

# rent(): Contrassegna il film come noleggiato se non è già noleggiato. Se il film non è già noleggiato imposta is_rented a True, altrimenti stampa il messaggio "Il film {self.title} è già noleggiato."
# return_movie(): Contrassegna il film come restituito. Se il film è già noleggiato imposta is_rented a False, altrimenti stampa il messaggio "Il film {self.title} non è attualmente noleggiato."
# 2. Classe Customer:

# Attributi:

# customer_id: str - Identificativo del cliente.
# name: str - Nome del cliente.
# rented_movies: list[Movie] - Lista dei film noleggiati.
# Metodi:

# rent_movie(movie: Movie): Aggiunge il film nella lista rented_movies se non è già stato noleggiato, altrimenti stampa il messaggio "Il film {movie.title} è già noleggiato."
# return_movie(movie: Movie): Rimuove il film dalla lista rented_movies se già presente, altrimenti stampa il messaggio "Il film {movie.title} non è stato noleggiato da questo cliente."
# 3. Classe VideoRentalStore:

# Attributi:

# movies: dict[str, Movie] - Dizionario che ha per chiave l'id del film e per valore l'oggetto Movie.
# customers: dict[str, Customer] - Dizionario che ha per chiave l'id del cliente e per valore l'oggetto Customer.
# Metodi:

# add_movie(movie_id: str, title: str, director: str): Aggiunge un nuovo film nel videonoleggio se non è già presente, altrimenti stampa il messaggio "Il film con ID {movie_id} esiste già."
# register_customer(customer_id: str, name: str): Iscrive un nuovo cliente nel videonoleggio se non è già presente, altrimenti stampa il messaggio "Il cliente con ID {customer_id} è già registrato."
# rent_movie(customer_id: str, movie_id: str): Permette al cliente di noleggiare un film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio "Cliente o film non trovato."
# return_movie(customer_id: str, movie_id: str): Permette al cliente di restituire un film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio "Cliente o film non trovato."
# get_rented_movies(customer_id: str): list[Movie] - Restituisce la lista dei film noleggiati dal client (customer.rented_movies) se il cliente esiste nel videonoleggio, altrimenti stampa il messaggio "Cliente non trovato." e ritorna una lista vuota.

class Movie:
    def __init__(self,movie_id:str,title:str,director:str) -> None:
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = False
    def rent(self):
        if self.is_rented:
            self.is_rented = False
            print(f"Il film {self.title} è già noleggiato.")
        else:
            self.is_rented = True
    def return_movie(self):
        if self.rent():
            self.is_rented = False
        else:
            self.is_rented = True
            print(f"Il film {self.title} non è attualmente noleggiato.")
            
class Customer:
    def __init__(self,customer_id:str,name:str) -> None:
        self.customer_id = customer_id
        self.name = name
        self.rented_movie :list[Movie]= []
    def rent_movie(self,movie:Movie):
        if movie.is_rented:
            self.rented_movie.append(movie)
        else:
            print(f"Il film {movie.title} è già noleggiato.")
    def return_movie(self,movie:Movie):
        if movie in self.rented_movie:
            self.rented_movie.remove(movie)
        else:
            print(f"Il film {movie.title} non è stato noleggiato da questo cliente.")
class VideoRentalStore:
    def __init__(self,movies:dict[str,Movie],customers:dict[str,Customer]) -> None:
        self.movies = movies
        self.customers = customers
    def add_movie(self,movie_id: str, title: str, director: str): 
        if movie_id not in self.movies:
            new_movie = Movie(movie_id,title,director)
            self.movies[movie_id] = new_movie
        else:
            print(f"Il film con ID {movie_id} esiste già.")
    def register_customer(self,customer_id: str, name: str):
        if customer_id not in self.customers:
            new_customer = Customer(customer_id,name)
            self.movies[customer_id] = new_customer
        else:
            print(f"Il cliente con ID {customer_id} è già registrato.")
    def rent_movie(self,customer_id: str, movie_id: str):
        if customer_id in self.customers and movie_id in self.movies:
            pass
            
        else:
            print("Cliente o film non trovato.")
    
#Scrivi una funzione che prenda un dizionario e un valore, e ritorni la prima chiave che corrisponde a quel valore, o None se il valore non è presente.
def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
    for key,value in dizionario.items():
        if value == valore:
            return key
        
print(trova_chiave_per_valore({'a': 100, 'b': 200, 'c': 300}, 200))
print(trova_chiave_per_valore({'k1': 'v1', 'k2': 'v2'}, 'v3'))

#Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.
        
def classifica_numeri(lista: int) -> dict[str:list[int]]:
    lista_pari = []
    lista_dispari = []
    for num in lista:
        if num %2 == 0:
            lista_pari.append(num)
        else:
            lista_dispari.append(num)
    dizionario = {"pari": lista_pari, "dispari": lista_dispari}
    return dizionario
    
print(classifica_numeri([1, 2, 3, 4, 5, 6])) 
print(classifica_numeri([]))

#Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.
def frequency_dict(elements: list) -> dict:
    dizionario = {}
    for elem in elements:
        if elem in dizionario:
            dizionario[elem] += 1
        else:
            dizionario[elem] = 1
    return dizionario
    
print(frequency_dict(['mela', 'banana', 'mela']))

# 1. Classe Base: Veicolo
# Crea una classe base chiamata Veicolo con i seguenti attributi e metodi:
# Attributi:
# - marca (stringa)
# - modello (stringa)
# - anno (intero)
# Metodi:
# - __init__(self, marca, modello, anno): metodo costruttore che inizializza gli attributi marca, modello e anno.
# - descrivi_veicolo(self): metodo che stampa una descrizione del veicolo nel formato "Marca: [marca], Modello: [modello], Anno: [anno]".
# 2. Classe Derivata: Auto
# Crea una classe derivata chiamata Auto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
# Attributi:
# - numero_porte (intero)
# Metodi:
# - __init__(self, marca, modello, anno, numero_porte): metodo costruttore che inizializza gli attributi della classe base e numero_porte.
# - descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il - numero di porte nella descrizione, nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Numero di porte: [numero_porte]".
# 3. Classe Derivata: Moto
# Crea una classe derivata chiamata Moto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
# Attributi:
# - tipo (stringa, ad esempio "sportiva", "cruiser", ecc.)
# Metodi:
# - __init__(self, marca, modello, anno, tipo): metodo costruttore che inizializza gli attributi della classe base e tipo.
# - descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il tipo di moto nella descrizione, nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Tipo: [tipo]".
class Veicolo:
    def __init__(self,marca:str,modello:str,anno:int) -> None:
        self.marca = marca
        self.modello = modello
        self.anno = anno
    def descrivi_veicolo(self):
        print(f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}')
class Auto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int,num_porte:int) -> None:
        super().__init__(marca, modello, anno)
        self.num_porte = num_porte
    def descrivi_veicolo(self):
        print(f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.num_porte}')
class Moto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int,tipo:str) -> None:
        super().__init__(marca, modello, anno)
        self.tipo = tipo
    def descrivi_veicolo(self):
        print(f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}')
    
veicolo = Veicolo("Generic", "Model", 2020)
auto = Auto("Toyota", "Corolla", 2021, 4) 
moto = Moto("Yamaha", "R1", 2022, "sportiva")  
veicolo.descrivi_veicolo()  
auto.descrivi_veicolo()  
moto.descrivi_veicolo()  
    
            
        