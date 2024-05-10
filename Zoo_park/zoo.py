class ZooKeeper:
    def __init__(self,
                 name: str,
                 surname: str,
                 id: str):
        self.name = name
        self.surname = surname
        self.id = id
        
    def feed_animals(self, animals):
        pass
    
    def clean_enclosures(self, enclosures):
        pass

class Animal:
    def __init__(self,
                 name: str,
                 species: str,
                 age: int,
                 height: float,
                 width: float,
                 preferred_habitat: str):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / age), 3)
        
    def __str__(self):
        return f"{self.name} ({self.species}), Age: {self.age}, Health: {self.health}"

class Fence:
    def __init__(self,
                 area: float,
                 temperature: float,
                 habitat: str):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = []
        
    def add_animal(self, animal):
        self.animals.append(animal)
        
    def __str__(self):
        return f"Fence: Area={self.area}, Temperature={self.temperature}, Habitat={self.habitat}, Animals={len(self.animals)}"

class Zoo:
    def __init__(self):
        self.fences = []
        self.guardians = []
        
    def add_fence(self, fence):
        self.fences.append(fence)
        
    def add_guardian(self, guardian):
        self.guardians.append(guardian)
