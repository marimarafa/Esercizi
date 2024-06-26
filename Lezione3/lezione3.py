#marim arafa
#26-04-2024

"""
4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
• Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
"""
pizzas = ["peperoni","margherita","sea food"]
for pizza in pizzas:
    print(f'I like {pizza} pizza')
print("I really love pizza ! \n")

"""
4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
• Modify your program to print a statement about each animal, such as A dog would make a great pet.
• Add a line at the end of your program, stating what these animals have in common. You could print a sentence, such as Any of these animals would make a great pet!
"""
animals = ["cat","dog","hamster"]
for animal in animals:
    print(f'A {animal} would mak a great pet.')
print("Any of these animals would make a great pet! \n")

"""
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive
"""
for n in range(1,20 +1):
    print(n)
print("\n")

"""
4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
(If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)
"""
numbers = list(range(1, 1000000 +1))
#for num in numbers:
#    print(num)
print("\n")

"""
4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts
at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers
"""
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print("\n")

"""
4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number
"""
for num in range(1,20,2):
    print(num)
print("\n")

"""
4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.
"""
multiples3 = []
for num in range(3, 30 +1, 3):
    multiples3.append(num)
print(multiples3,"\n")

"""
4-8,9. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the 
first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
"""
cube_numbers = [n** 3 for n in range(1, 10 +1)]
print(cube_numbers,"\n")
"""
4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.
"""
#usare la lista dichiarata nell'esercizio 4-7
print(f'The first three items in the list are :.{multiples3[:3]}')
print(f'The middle three items in the list are :.{multiples3[3:6]}')
print(f'The last three items in the list are :.{multiples3[-3:]}\n')

"""
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list.Print the
message My friend’s favorite pizzas are:,and then use a for loop to print the second list.Make sure each new pizza is stored in the appropriate list.
"""
#usare la lista dichiarata nell'esercizio 4-1
friend_pizzas = pizzas.copy()
pizzas.append("capricciosa")
friend_pizzas.append("4 formaggi")
for pizza in pizzas:
    print(f'My favorite pizzas are: {pizza}')
print("\n")
for pizza in friend_pizzas:
    print(f'My friend’s favorite pizzas are: {pizza}')
print("\n")

"""
4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. 
Choose a version of foods.py, and write two for loops to print each list of foods.
"""
#exercise to do
"""
5-1. Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results 
of each test. Your code should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.
"""
car = 'subaru'
print("1/ Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\n2/ Does car start with the letter 's'? I predict True.")
print(car.startswith('s'))

print("\n3/ Is car is not 'ferrari'? I predict True.")
print(car != 'ferrari')

print("\n4/ Is car lenght is 6? I predict True.")
print(len(car) == 6)

print("\n5/ Is car in the list of cars? I predict True.")
cars = ['subaru', 'ferrari', 'mercedes']
print(car in cars)

print("\n6/ Is car type is 'audi'? I predict False.")
print(car == 'audi')

print("\n7/ Is the length of the car 8 ? I predict False.")
print(len(car) == 8)

print("\n8/ Is car not in the list of cars? I predict False.")
print(car not in cars)

print("\n9/ Is car a number ? I predict False.")
print(car.isnumeric())

print("\n10/ Is car start with the letter 'f'? I predict False")
print(car.startswith('f'),"\n")

"""
5-2. More Conditional Tests: You don’t have to limit the number of tests you cre-
ate to 10. If you want to try more comparisons, write more tests and add them

to conditional_tests.py. Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
"""
#• Tests for equality and inequality with strings
name1 = "marco"
name2 = "SOFIA"
print(f'Tests for equality with strings: {name1},{name2}')
print(name1 == name2)
print(f'Tests for inequality with strings: {name1},{name2}')
print(name1 != name2)

#• Tests using the lower() method
print(f'\n Tests using the lower() method: {name1},{name2}')
print(name1.lower() == name2.lower())

#• Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
number1 = 34
number2 =45
print(f'\n Numerical tests:{number1},{number2}')
print(number1 == number2)  
print(number1 != number2)  
print(number1 > number2)   
print(number1 < number2)  
print(number1 >= number2)  
print(number1 <= number2)  

#• Tests using the and keyword and the or keyword
print(f'\n Tests using the and keyword and the or keyword :{number1},{number2}')
print(number1 > 5 and number1 < 50)
print(number2 > 100 or number2 > 1005)

#• Test whether an item is in a list
lista = [2,3,4,5]
print(f'\n Test whether an item is in list: {lista}')
print(4 in lista)

#• Test whether an item is not in a list
print(f'\n Test whether an item is not in list: {lista}')
print(5  not in lista,"\n")

"""
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
• Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)
"""
alien_colour = "green"
if alien_colour == "green":
    print("the player just earned 5 points.\n")
alien_colour2 = "red"
if alien_colour2 == "green":
    print("the player just earned 5 points.\n")

"""
5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned 10 points.
• Write one version of this program that runs the if block and another that runs the else block.
"""
#utilizzare le variabili dichiarate nell'esercizio  5-3
if alien_colour == "green":
    print("the player just earned 5 points for shooting the alien.\n")
else:
    print("the player just earned 10 points for shooting the alien.\n")
if alien_colour2 != "red":
     print("the player just earned 5 points for shooting the alien.\n")
else:
    print("the player just earned 10 points for shooting the alien.\n")

"""
5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed for the appropriate color alien.
"""
#utilizzare le variabili dichiarate nell'esercizio  5-3
if alien_colour == "green":
    print("the player just earned 5 points.\n")
elif alien_colour == "yellow":
    print("the player just earned 10 points.\n")
else:
    print("the player just earned 15 points.\n")

if alien_colour2 == "green":
    print("the player just earned 5 points.\n")
elif alien_colour2 == "yellow":
    print("the player just earned 10 points.\n")
else:
    print("the player just earned 15 points.\n")


if alien_colour != "green":
    print("the player just earned 5 points.\n")
elif alien_colour != "yellow":
    print("the player just earned 10 points.\n")
else:
    print("the player just earned 15 points.\n")

"""
5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
• If the person is less than 2 years old, print a message that the person is a baby.
• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that the person is an adult.
• If the person is age 65 or older, print a message that the person is an elder.
"""
person_age = 20
if person_age < 2:
    print("The person is a baby\n")
elif person_age >= 2 and person_age < 4:
    print("The person is a toddler.\n")
elif person_age >= 4 and person_age < 13:
    print("The person is a kid.\n")
elif person_age >= 13 and person_age < 20:
    print("The person is a teenager.\n")
elif person_age >= 20 and person_age < 65:
    print("The person is an adult.\n")
elif person_age >= 65:
    print("The person is an elder.\n")

"""
5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like Apples!
"""
favourite_fruits = ["apple","mango","banana"]
if "apple" in favourite_fruits:
    print("You really like Apple!")
if "banana" in favourite_fruits:
    print("You really like Banana!")
if "mango" in favourite_fruits:
    print("You really like Mango!")
if "orange" in favourite_fruits:
    print("You really like Orange!")
if "cherries" in favourite_fruits:
    print("You really like Cherries!")
print("\n")

"""
5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user.
• If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.
"""
usernames = ["admin","luca","carlo","claudia","sofia"]
for username in usernames:
    if username is not "admin":
        print(f'Hello {username} ,thank you for logging in again')
    else:
        print("Hello admin, would you like to see a status report?")
print("\n")

"""
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct message is printed.
"""
usernames.clear()
if not usernames:
    print("We need to find some users!\n")

"""
5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to
enter a new username. If a username has not been used, print a message saying that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to 
make a copy of current_users containing the lowercase versions of all existing users.)
"""
current_users = ["nicola","PAOLO","bob","alice","SILVIA"]
current_users_low = [user.lower() for user in current_users]
new_users = ["paolo","silvia","fabrizio","sam","nina"]
for person in new_users:
    if person in current_users_low:
        print(f'{person} will need to enter a new username')
    else:
        print(f'{person} username is available')
print("\n")
    
"""
5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
• Store the numbers 1 through 9 in a list.
• Loop through the list.
• Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
7th 8th 9th", and each result should be on a separate line.
"""
ordinal_numbers = [1,2,3,4,5,6,7,8,9]
for num in ordinal_numbers:
    if num == 1:
        print(f'{num}st')
    elif num == 2:
        print(f'{num}nd')
    elif num == 3:
        print(f'{num}rd')
    else:
        print(f'{num}th')