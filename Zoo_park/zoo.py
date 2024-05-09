class Zoo_keeper:
    def __init__(self,
                 name:str,
                 surname :str,
                 id:str):
        self.name = name 
        self.surname = surname
        self.id = id
        
    
class Animal:
    def __init__(self,
                 name:str,
                 species: str,
                 age:int,
                 height:float,
                 widht:float,
                 preferred_habitat:str,
                 health:float) :
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.widht = widht
        self.pref_hab = preferred_habitat
        self.health = health
    def add_animal(self):
        pass
        
            
     
class Fence:
    def __init__(self,
                 animals:Animal,
                 area:float,
                 temperature:float,
                 habitat:str) :
        self.animals =animals
        self.area = area
        self.temperature = temperature
        self.habitat = habitat  
class Zoo:
    def __init__(self,
                 fences:Fence,
                 guradians:Zoo_keeper):
        self.fences = fences
        self.guradians = guradians  
    