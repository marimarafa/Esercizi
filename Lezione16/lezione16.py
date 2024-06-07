# Obiettivo:
# Implementare una classe Media che rappresenti un media generico (ad esempio, un film o un libro) e una classe derivata Film che rappresenti specificamente un film. Gli studenti dovranno anche creare oggetti di queste classi, aggiungere valutazioni e visualizzare le recensioni.

# Specifiche della Classe Media:
 
# Attributi:
# - title (stringa): Il titolo del media.
# - reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5.

# Metodi:
# - set_title(self, title): Imposta il titolo del media.
# - get_title(self): Restituisce il titolo del media.
# - aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
# - getMedia(self): Calcola e restituisce la media delle valutazioni.
# - getRate(self): Restituisce una stringa che descrive il giudizio medio del media basato sulla media delle valutazioni.
# - ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
# - recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo, il voto medio, il giudizio e le percentuali di ciascun voto. Esempio di riassunto:
 
# Titolo del Film: The Shawshank Redemption
# Voto Medio: 3.80
# Giudizio: Bello
# Terribile: 10.00%
# Brutto: 10.00%
# Normale: 10.00%
# Bello: 30.00%
# Grandioso: 40.00%

# Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film, aggiunga a ognuno dei due almeno dieci valutazioni e richiami il metodo recensione().
class Media:
    def __init__(self,title:str,reviews:list[int]) -> None:
        self.title = title 
        self.reviews = reviews

    def set_title(self,title):
        self.title = title

    def get_title(self):
        return self.title
    
    def aggiungi_valutazione(self,voto):
        if 1 <= voto >=5:
            self.reviews.append(voto)
    
    def get_media(self):
        media = sum(self.reviews) / len(self.reviews)
        return round(media,3)
    
    def get_rate(self):
        percentuale_media :float = self.get_media()
        if 1 > percentuale_media:
            return "Terribile"
        if 2 > percentuale_media:
            return "Brutto"
        if 3 > percentuale_media:
            return "Normale"
        if 4 > percentuale_media:
            return "Bello"
        if 5 > percentuale_media:
             return "Grandioso"
        
    def rate_percentage(self,voto :float):
            return  f'{voto *10 }%'
        
    def recensione(self):
        return f'Titolo del Film: {self.get_title()}\nVoto Medio: {self.get_media()}\nGiudizio: {self.get_rate()}\nTerribile: {self.rate_percentage(1.0)}\nBrutto: {self.rate_percentage(2.0)}\nNormale: {self.rate_percentage(3.0)}\nBello: {self.rate_percentage(4.0)}\nGrandioso: {self.rate_percentage(5.0)}'
        
film1 :Media = Media(title= "The Shawshank Redemption",reviews=[2,3,4,5,3,2,1,3,4,2,3,5])
print(film1.recensione())       
        


        