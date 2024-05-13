class Animal:
    def __init__(self,
                 species :str,
                 age :int,
                 name :str) -> None:
        self.species = species
        self.age = age
        self.name = name

    def __str__(self) -> str:
        return (f{self.__class__.name}'name = {self.name},species :{self.species} , age :{self.age}')

class Cat(Animal):
    def __init__(self,
                  species: str,
                    age: int,
                    name :str) -> None:
        super().__init__(name ,species, age)
        self.name = name
    
class Rabbit(Animal):
    def __init__(self,
                  species: str,
                    age: int,
                    name :str) -> None:
        super().__init__(name ,species, age)
        self.name = name

class Person(Animal):
    def __init__(self,
                  species: str,
                    age: int,
                    name :str,
                    surname :str,
                    cf:str) -> None:
        super().__init__(name,species, age)

        self.name  = name
        self.surname = surname
        self.cf = cf
    def __str__(self) -> str:
        s = super().__str__()[:-1]
        s += f'{self.name.capitalize()},{self.surname.capitalize()},cf = {self.cf},age ={self.age}, species :{self.species}'

    
class Student(Person):
    def __init__(self,
                  species: str,
                    age: int,
                      name: str,
                        cf: str,
                        matricula :str) -> None:
        super().__init__(name ,species, age, name, cf)

        self.matricula = matricula

persona :Person = Person(name="marim",surname= "arafa",cf="87699",age=32,species="ilu")
animale :Animal = Animal(name = "Willy",species="balena", age =33)
print(persona)
print(animale)
gatto :Cat= Cat(name="Grafield",species="ksc",age=12) 
print(gatto)


        


