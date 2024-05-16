#marim arafa
#8-5-2024
"""9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() 
that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open. Make an instance called restaurant from your class.
Print the two attributes individually, and then call both methods.
"""
class Restaurant:
    def __init__(self,
                 name :str,
                 cuisine :str,
                 number_served:int= 0) -> None:
        self.name = name 
        self.cuisine = cuisine
        self.number_served = number_served

    def describe_restaurant(self):
        return(f'name of the restauranrt :{self.name}, cuisine type :{self.cuisine}')
    def open_restaurant(self):
        return(f"The restaurant is open!! number of people served :{self.number_served}")
    def set_number_served(self,new_num_served):
        self.number_served = new_num_served
        return f'number to serve:{new_num_served}'
    def increment_number_served(self):
        while self.number_served:
            self.number_served += 1
            return f' number to serve :{self.number_served}'

        
        
restaurant1 :Restaurant = Restaurant(name="ndfsvk",cuisine="vmdcwdc",number_served= 0)
print(restaurant1.describe_restaurant())
print(restaurant1.open_restaurant(),"\n")
print(restaurant1.set_number_served(7))
print(restaurant1.increment_number_served())
print(restaurant1.increment_number_served())
print(restaurant1.increment_number_served())

"""9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.
"""
restaurant2 :Restaurant = Restaurant(name = "djvedv", cuisine="jnvkedv")
restaurant3:Restaurant = Restaurant(name="ixcjs", cuisine="scfwef")
print(restaurant2.describe_restaurant())
print(restaurant3.describe_restaurant(),"\n")

"""9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored
 in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a
personalized greeting to the user. Create several instances representing different users, and call both methods for each user.
"""
class User:
    def __init__(self,
                  first_name :str,
                 last_name :str,
                 email :str,
                 password :int,
                 num_phone : int,
                 login_attempts :int) -> None:
        
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.num_phone = num_phone
        self.login_attempts = login_attempts

    def describe_user(self):
        return f'user name :{self.first_name} {self.last_name}, email :{self.email}, password :{self.password}: phone number :{self.num_phone}'
    def great_user(self):
        return f'Welcome {self.first_name} {self.last_name}! It is great to see you'
    def increment_login_attempts(self):
        while self.login_attempts:
            self.login_attempts += 1
            return f'login attempts :{self.login_attempts}'
    def reset_login_attempts(self):
        while self.login_attempts > 0:
            self.login_attempts -=1
            print(f'you have  {self.login_attempts+1} login attempts left')
            if self.login_attempts == 0:
                return("You have 0 login attempts")   
    
user1 :User = User(first_name= "marco", last_name= "rossi",email="marcorossi32@gmail.com" ,password= 215435,num_phone= 467879700,login_attempts= 3)
user2 :User = User(first_name= "luca", last_name= "verdi",email="verdiluca@gmail.com" ,password= 4335578,num_phone= 466646460,login_attempts=3)
user3 :User = User(first_name= "alice", last_name= "gialli",email="malicegialli@gmail.com" ,password= 56765785,num_phone= 46787575450,login_attempts=3)
print(user1.describe_user(),"\n",user1.great_user())
print(user2.describe_user(),"\n",user2.great_user())
print(user3.describe_user(),"\n",user3.great_user())
print(user2.increment_login_attempts())
print(user2.increment_login_attempts())
print(user2.reset_login_attempts())



"""9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class.
 Print the number of customers the restaurant has served, and then change this value and print it again. Add a method called set_number_served() that lets you set the number of customers that
have been served. Call this method with a new number and print the value again. Add a method called increment_number_served() that lets you increment the number of customers who’ve been served.
 Call this method with any number you like that could represent how many customers were served in, say, a day of business. 
"""
#esercizio risolti dentro esercizio 9-1
"""9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. Write a method called increment_login_attempts() that increments the value of login_attempts 
by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts() several times. Print 
the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.
"""
#esercizio risolto dentro esercizio 9-3

"""9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1  or Exercise 9-4.
 Either version of the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors.
 Create an instance of IceCreamStand, and call this method
"""
class IceCreamStand(Restaurant):
    def __init__(self,
                  name: str,
                    cuisine: str,
                      number_served: int = 0,
                    flavors:list[str] = []) -> None:
        super().__init__(name, cuisine, number_served)
        self.flavors = flavors

    def iceCream_falvors(self):
        print("\nIce cream flavors:")
        for flavor in self.flavors:
            print(f'    {flavor}')

ice_cream :IceCreamStand = IceCreamStand(name = "jcs", cuisine = "jfenfgel",flavors=["strawberry","lemon","chocolate"])
ice_cream.iceCream_falvors()

"""9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 or Exercise 9-5. Add an attribute, privileges, 
that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges() that lists the administrator’s set of privileges.
 Create an instance of Admin, and call your method.
"""
class Admin(User):
    def __init__(self, first_name: str,
                  last_name: str,
                    email: str,
                      password: int,
                        num_phone: int,
                          login_attempts: int,
                          previleges :list[str] = []) -> None:
        super().__init__(first_name, last_name, email, password, num_phone, login_attempts)
        self.previleges = previleges
    
    def show_previleges(self):
        print(f'\nThe admin {self.first_name} can:')
        for prev in self.previleges:
            print(prev)
admin :Admin = Admin(first_name= "sofia",last_name="Bob",email="sofiabob23@gmail.com",password=767934,num_phone=33256788,login_attempts=5,previleges=["delete post","ban user","add post"])
admin.show_previleges()

"""9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. Move the show_privileges()
 method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges.
"""
class Privileges:
    def __init__(self,
                 privileges : list[str]) -> None:
        self.privileges = privileges
        













    
        


      
