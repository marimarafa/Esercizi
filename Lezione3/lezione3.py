#marim arafa
#23-4-2024

"""
8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in 
this chapter. Call the function, and make sure the message displays correctly.
"""
def display_message(message:str)-> str:
    print(message)
display_message("What are you learning about in this lesson? \n")

"""
8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message,
such as "One of my favorite books is Alice in Wonderland". Call the function, making sure to include a book title as an argument
in the function call.
"""
def favorite_book(title :str)-> str:
    print(f'One of my favorite book is {title}')
favorite_book("Dream of the Red Chamber (紅樓夢)")

"""
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the 
shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function
once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
"""
def make_shirt(size:int ,message :str) -> str:
    print(f'Size shirt: {size} , Message: {message}')
size = "Small"
message = "Have a good day"    
make_shirt(size,message)
print("\n")

"""
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
"""
make_shirt("Large","I love python")
make_shirt("Medium","I love python")
make_shirt("Xsmall","..,..")
print("\n")

"""
8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a 
simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three
different cities, at least one of which is not in the default country
"""
def describe_city(city:str , country:str) -> str:
    print(f'{city} is in {country}')
describe_city("Rome","Italy")
describe_city("London","England")
describe_city("Cairo","Egypt")
print("\n")

"""
8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. The function should
return a string formatted like this: "Santiago, Chile". Call your function with at least three city-country pairs, 
and print the values that are returned.
"""
def city_country(city :str,country :str) -> str:
    return city,country
city_and_country1 = city_country("Santiago","Chile")
city_and_country2 = city_country("Rome","Italy")
city_and_country3 = city_country("Tokyo","Japan")
print(city_and_country1)
print(city_and_country2)
print(city_and_country3)
