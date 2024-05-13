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
    
    def clean_fences(self, fences):
        pass
    
    def __str__(self):
        return f"Zoo keeper: name={self.name},surname={self.surname},id={self.id}"

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
        return f"Animal : name= {self.name} ,speces= {self.species},age= {self.age},height= {self.height},width= {self.width},preffered habitat= {self.preferred_habitat},health= {self.health}"        

class Fence:
    def __init__(self,
                 height: float,
                 width : float,
                 temperature: float,
                 habitat: str):
        
        self.height = height
        self.width = width
        self.area = self.height * self.width
        self.temperature = temperature
        self.habitat = habitat
        self.animals = []
        
    def __str__(self):
        return f"Fence: area={self.area},temperature={self.temperature},habitat={self.habitat},animals={len(self.animals)}"

class Zoo:
    def __init__(self,
                 fence:Fence,
                 guradians :ZooKeeper):
        
        self.fences = fence
        self.guardians = guradians
        
    def add_animal(self,animal:Animal,fence:Fence):
        for fence in self.fences:
            if animal not in fence:
                if animal.preferred_habitat == fence.habitat and fence.area > len(fence.animals):
                    fence.animals.append(animal)
                    fence.area = fence.area - (self.height * self.width)
                    return f"{animal.name} è stato aggiunto al recinto {fence},l'area libera rimasta nel recinto è {fence.area}."
                else:  
                    return f"Non ci sono recinti adatti o spazio disponibile per questo animale."
                
    def remove_animal(self,animal:Animal):
        for fence in self.fences:
            if animal in fence.animals:
                fence.animals.remove(animal)
                fence.area = fence.area + (animal.height * animal.width)
                return f"{animal.name} è stato rimosso dal recinto {fence}, l'area libera nel recinto è stata aggiornata a {fence.area}."
            else:
                return f"L'animale {animal.name} non è presente in nessun recinto."
                
    def add_fence(self, fence:Fence):
        self.fences.append(fence)
        
    def add_guardian(self, guardian:ZooKeeper):
        self.guardians.append(guardian)

animale: Animal=Animal("pippo","cane",34,3.4,4.5,"giungla")
recinto :Fence = Fence(17.9,23.6,45.0,"giungla")
print(Zoo.add_animal(animale,recinto))