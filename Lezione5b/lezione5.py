#marim arafa
#8-5-2024
"""9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() 
that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open. Make an instance called restaurant from your class.
Print the two attributes individually, and then call both methods.
"""
class Restaurant:
    def __init__(self,name :str,cuisine :str) -> None:
        self.name = name 
        self.cuisine = cuisine
    def describe_restaurant(self):
        return(f'name of the restauranrt :{self.name}, cuisine type :{self.cuisine}')
    def open_restaurant(self):
        return("The restaurant is open!!")

restaurant1 :Restaurant = Restaurant(name="ndfsvk",cuisine="vmdcwdc")
print(restaurant1.describe_restaurant())
print(restaurant1.open_restaurant())
