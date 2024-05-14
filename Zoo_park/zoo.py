class Zoo:
    def __init__(self, fences: list = [], zoo_keepers: list = [])-> None:
        self.fences = fences
        self.zoo_keepers = zoo_keepers

    def get_zoo_keepers(self):
        return self.zoo_keepers

    def get_fences(self):
        return self.fences

    def add_animal(self, animal, fence):
            if fence.area >= animal.height * animal.width and animal.preferred_habitat == fence.habitat:
                fence.animals.append(animal)
                return(f"{animal.name} aggiunto al {fence.habitat} recinto,spazio rimanente:{fence.area}")
            else:
                return (f"L'animale {animal.name} non è stato aggiunto nel {fence.habitat} recinto.")

    def remove_animal(self, animal, fence):
        if animal in fence.animals:
            fence.animals.remove(animal)
            return (f"{animal.name} rimosso dal {fence.habitat} recinto. area del recinto {fence.area}")

    def describe_zoo(self):
        print("Guardians:")
        for guardian in self.get_zoo_keepers():
            print(guardian)
        print("\nFences:")
        for fence in self.get_fences():
            print(fence)
            print("with animals:")
            for animal in fence.animals:
                print(animal)
        print("#" * 30)

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

    def add_animal(self, animal):
        if not self.area >= animal.height * animal.width(animal):
            print(f"non c'e abbastanza spazio per questo animale")
        if animal not in self.animals:
            self.animals.append(animal)
            return self.area == self.area - (animal.height * animal.width)

    def remove_animal(self, animal):
        if animal not in self.animals:
            return("Animal not in fence")
        else:
            self.animals.remove(animal)
            return self.area == self.area + (animal.height * animal.width)

    def __str__(self):
        return f"Fence(area={self.area}, temperature={self.temperature}, habitat={self.habitat})"
    
    
class ZooKeeper:
    def __init__(self, name, surname, id):
        self.name = name
        self.surname = surname
        self.id = id

    def feed(self, animal,fence):
            if fence.area >= animal.height * animal.width:
                animal.health += 1
                animal.height *= 1.02
                animal.width *= 1.02
            return(f"Fed {animal.name} , animal height:{round(animal1.height)*3},animal health: {round(animal.health)*3}, animal width: {round(animal.width)*3}")

    def clean(self, fence):
        occupied_area = sum(animal.height * animal.width for animal in fence.animals)
        remaining_area = fence.area - occupied_area
        if remaining_area == 0:
            return occupied_area
        return occupied_area / remaining_area

    def __str__(self):
        return f"ZooKeeper(name={self.name}, surname={self.surname}, id={self.id})"




fence1 = Fence(100.32, 25, "Continentale")
fence2 = Fence(140, 55, "Jungle")
zoo_keeper1 = ZooKeeper("Lorenzo", "Maggi", 1234)
zoo_keeper2= ZooKeeper("Luca", "rossi", 2335)
zoo = Zoo()
zoo.zoo_keepers.append(zoo_keeper1)
zoo.zoo_keepers.append(zoo_keeper2)
zoo.fences.append(fence1)
zoo.fences.append(fence2)
animal1 = Animal("Scoiattolo", "Blabla", 25.8, 10, 10, "Continentale")
animal2 = Animal("Lupo", "Lupus", 14.7, 20, 20.8, "Continentale")
(zoo.describe_zoo)
print(zoo.add_animal(animal1, fence1))
print(zoo.add_animal(animal2, fence1))
print(zoo.remove_animal(animal1,fence2))
zoo_keeper1 = ZooKeeper("Lorenzo", "Maggi", 1234)
zoo_keeper2= ZooKeeper("Luca", "rossi", 2335)
#zoo_keepers = (zoo.zoo_keepers(zoo_keeper1,zoo_keeper2))
#zoo = Zoo(zoo_keepers)
print(zoo_keeper1.feed(animal1,fence1))
print(zoo_keeper1.feed(animal2,fence1))