class Zoo:
    def __init__(self, 
                 fences: list = [],
                   zoo_keepers: list = [])-> None:
        self.fences = fences
        self.zoo_keepers = zoo_keepers

    def get_zoo_keepers(self):
        return self.zoo_keepers

    def get_fences(self):
        return self.fences

    def add_animal(self, animal, fence):
            if animal in fence.animals:
                return f'The {animal.name} already exist in this fence'
            if not fence.area >= animal.height * animal.width:
                return(f"There is no enough space for this animal in this fence.")
            if animal not in fence.animals and fence.area >= animal.height * animal.width and animal.preferred_habitat == fence.habitat:
                fence.animals.append(animal)
                fence.area -= (animal.height * animal.width)
                return(f"{animal.name} add into {fence.habitat} fence, remeaning area :{round(fence.area,3)}")
            if animal.preferred_habitat != fence.habitat:
                return (f"Cannot add {animal.name} in  {fence.habitat} fence.")

    def remove_animal(self, animal, fence):
        if animal not in fence.animals:
            return(f" The {animal.name} is not in this fence.")
        else:
            fence.animals.remove(animal)
            fence.area == fence.area + (animal.height * animal.width)
            return(f'Animal removed correctly! Area of the fence is now updated to : {round(fence.area,3)}')

    def describe_zoo(self):
        print("\nGuardians:\n")
        for guardian in self.get_zoo_keepers():
            print(guardian)
        print("\nFences:\n")
        for fence in self.get_fences():
            print(fence,"\n")
            print("with animals:\n")
            for animal in fence.animals:
                print(animal,"\n")
            print("#" * 30,"\n")

class Animal:
    def __init__(self,
                 name: str,
                 species: str,
                 age: int,
                 height: float,
                 width: float,
                 preferred_habitat: str)-> None:
        
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / age), 3)
        
    def __str__(self):
        return f"Animal(name={self.name}, species={self.species}, age={self.age})"


class Fence:
    def __init__(self,
                 area: float,
                 temperature: float,
                 habitat: str)-> None:
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = []
     

    def __str__(self):
        return f"Fence(area={self.area}, temperature={self.temperature}, habitat={self.habitat})"
    
    
class ZooKeeper:
    def __init__(self,
                  name: str,
                    surname:str,
                      id:str)-> None:
        self.name = name
        self.surname = surname
        self.id = id

    def feed(self, animal,fence):
            if fence.area > animal.height * animal.width:
                animal.health *= 1.01
                animal.height *= 1.02
                animal.width *= 1.02
            return(f"Fed {animal.name} , animal height:{round(animal.height,3)},animal health: {round(animal.health,3)}, animal width: {round(animal.width,3)}")

 
    def clean(self, fence):
        for animal in fence.animals:
            occupied_area = animal.height * animal.width
            remaining_area = fence.area - occupied_area
            if remaining_area <= 0 :
                return round(occupied_area,3)
            else:
                return round(occupied_area / remaining_area,3)

    def __str__(self):
        return f"ZooKeeper(name={self.name}, surname={self.surname}, id={self.id})"


fence1 = Fence(1000.32, 25.4, "Continent")
fence2 = Fence(140, 55.4, "Jungle")
zoo_keeper1 = ZooKeeper("Lorenzo", "Maggi", 1234)
zoo_keeper2= ZooKeeper("Luca", "rossi", 2335)
zoo = Zoo()
zoo.zoo_keepers.append(zoo_keeper1)
zoo.zoo_keepers.append(zoo_keeper2)
zoo.fences.append(fence1)
zoo.fences.append(fence2)
animal1 = Animal("Scoiattolo", "Blabla", 25.8, 10.8, 10.8, "Continent")
animal2 = Animal("Lupo", "Lupus", 14.7, 20.7, 20.8, "Continent")
animal3 = Animal("pippo", "gghi", 1.0, 2.99, 2.8, "Jungle")

print(zoo.add_animal(animal1, fence1))
print(zoo.add_animal(animal1, fence1))
print(zoo.add_animal(animal2, fence1))
print(zoo.add_animal(animal3, fence2))
print(zoo.remove_animal(animal1,fence2))
zoo_keeper1 = ZooKeeper("Lorenzo", "Maggi", 1234)
zoo_keeper2= ZooKeeper("Luca", "rossi", 2335)
print(zoo_keeper1.feed(animal1,fence1))
print(zoo_keeper1.feed(animal2,fence1))
print(zoo_keeper1.clean(fence1))
print(zoo_keeper1.clean(fence2))
zoo.describe_zoo()