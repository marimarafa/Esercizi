class Movie:
    def __init__(self, movie_id: str, title: str, director: str) -> None:
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = False

    def rent(self):
        if self.is_rented:
            print(f"Il film {self.title} è già noleggiato.")
        else:
            self.is_rented = True

    def return_movie(self):
        if self.is_rented:
            self.is_rented = False
        else:
            print(f"Il film {self.title} non è attualmente noleggiato.")

class Customer:
    def __init__(self, customer_id: str, name: str) -> None:
        self.customer_id = customer_id
        self.name = name
        self.rented_movie: list[Movie] = []

    def rent_movie(self, movie: Movie):
        if not movie.is_rented:
            movie.rent()
            self.rented_movie.append(movie)
        else:
            print(f"Il film {movie.title} è già noleggiato.")

    def return_movie(self, movie: Movie):
        if movie in self.rented_movie:
            movie.return_movie()
            self.rented_movie.remove(movie)
        else:
            print(f"Il film {movie.title} non è stato noleggiato da questo cliente.")

class VideoRentalStore:
    def __init__(self) -> None:
        self.movies: dict[str, Movie] = {}
        self.customers: dict[str, Customer] = {}

    def add_movie(self, movie_id: str, title: str, director: str):
        if movie_id not in self.movies:
            new_movie = Movie(movie_id, title, director)
            self.movies[movie_id] = new_movie
        else:
            print(f"Il film con ID {movie_id} esiste già.")

    def register_customer(self, customer_id: str, name: str):
        if customer_id not in self.customers:
            new_customer = Customer(customer_id, name)
            self.customers[customer_id] = new_customer
        else:
            print(f"Il cliente con ID {customer_id} è già registrato.")

    def rent_movie(self, customer_id: str, movie_id: str):
        if customer_id in self.customers and movie_id in self.movies:
            customer = self.customers[customer_id]
            movie = self.movies[movie_id]
            customer.rent_movie(movie)
        else:
            print("Cliente o film non trovato.")

    def return_movie(self, customer_id: str, movie_id: str):
        if customer_id in self.customers and movie_id in self.movies:
            customer = self.customers[customer_id]
            movie = self.movies[movie_id]
            customer.return_movie(movie)
        else:
            print("Cliente o film non trovato.")

    def get_rented_movies(self, customer_id: str) -> list[Movie]:
        if customer_id in self.customers:
            customer = self.customers[customer_id]
            return customer.rented_movie
        else:
            print("Cliente non trovato")
            return []

# Creazione di un nuovo videonoleggio
videonoleggio = VideoRentalStore()

# Aggiunta di nuovi film
videonoleggio.add_movie("1", "Inception", "Christopher Nolan")
videonoleggio.add_movie("2", "The Matrix", "Wachowski Brothers")

# Registrazione di nuovi clienti
videonoleggio.register_customer("101", "Alice")
videonoleggio.register_customer("102", "Bob")

# Noleggio di film
videonoleggio.rent_movie("101", "1")
videonoleggio.rent_movie("102", "2")

# Tentativo di noleggiare un film già noleggiato
videonoleggio.rent_movie("101", "1")

# Restituzione di film
videonoleggio.return_movie("101", "1")

# Tentativo di restituire un film non noleggiato
videonoleggio.return_movie("101", "1")

# Ottenere la lista dei film noleggiati da un cliente
rented_movies_alice = videonoleggio.get_rented_movies("101")
print(f"Film noleggiati da Alice: {[movie.title for movie in rented_movies_alice]}")

rented_movies_bob = videonoleggio.get_rented_movies("102")
print(f"Film noleggiati da Bob: {[movie.title for movie in rented_movies_bob]}")

#output:
# Cliente o film non trovato.
# Cliente o film non trovato.
# Cliente o film non trovato.
# Cliente o film non trovato.
# Cliente o film non trovato.
# Cliente non trovato
# Film noleggiati da Alice: []
# Cliente non trovato
# Film noleggiati da Bob: []