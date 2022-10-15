# Salaa 100 Days of Code 

print ("Hello World!") # print fctn
print ("Hello Python World!") # print fctn 

message = "Hello Python" # varible
print(message) # print fctn

message_tem = "Hello Python Crash Course" # varible
print(message_tem) # print fctn

message_tem = "Hello Python Crash Course Reader" # varible
print(message_tem) # print fctn

sala = "Ada Lovelace" # variable
print(sala.title()) # first letters upper case method
print(sala.upper()) # upper case method
print(sala.lower()) # lower case method

# Using variables in strings
first_name = "ada" # variable
last_name = "lovelace" # varible
full_name = f"{first_name} {last_name}" # using variable and f-string
print(full_name) 

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!") 

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
nam=f"Hello, {full_name.upper()}!" 
print(nam)

fav_number = 8
favnumber = f"My favourite number is {fav_number}"
print(favnumber) 

# Use of single quotes and double quotes in strings
einstein = 'Albert Einstein once said, "A person who never made a mistake never tried anything new".' 
print(einstein) 
famous_person = "Albert Einstein"
mindset = '"A person who never made a mistake never tried anything new"'
mesage = f"{famous_person} once said, {mindset}"
print(mesage)
naj = "One of Python's strength is its diverse community."
print(naj) 

# Using whitespace; spaces, tabs--\t, end-of-line, newlines--\n 
print("Languages:\n\tPython\n\tC\n\tJavascript")

# Using underscore in numbers
age=10_00
print(age)
margin=100_0
print(margin)

# Mutiple variable assignment
x, y, z = 0, 0, 0

# Constants; a constant is a variable whose value stays the same throughout,
# the life of a program(mostly in uppercase letters)
MAX_CONNECTIONS = 5000

# Introducing Lists; list of items in a particular order, store sets of information in python 
bicycles = ['trek', 'canondale', 'redline', 'specialized']
print(bicycles) 
# Accessing items in a list 
print(bicycles[0].title())
print(bicycles[1].upper())
print(bicycles[-1])
print(bicycles[-2])
# Using individual items from a list 
content = f"My first bicycle was a {bicycles[0].title()}" 
print(content)
transport = ['train', 'bike']
fav_transport = f"'I would like to own a Honda {transport[1].title()}'"
print(fav_transport)
# Changing, Adding, and Removing Elements in a List 
motorcycles = ['honda', 'volvo', 'toyota']
print(motorcycles)
motorcycles[-1] = 'suzuki' # modifying elements in a list
print(motorcycles)
motorcycles.append('zumba') # appending elements in a list 
motorcycles.append('ducati') # appending elements in a list 
print(motorcycles)
motorcycles.insert(0, 'bajaj') # inserting elements in a list 
print(motorcycles)
# removing elements in a list 
del motorcycles[4]  
print(motorcycles)
# removing elements from a list using the pop() method,
# this method removes the last item on a list and lets you work with the element after removing it. 
last_owned = motorcycles.pop() 
print(motorcycles)
print(last_owned)
first_owned = motorcycles.pop(2) # removing an element from any position on the list using the pop() method,
print(motorcycles)
print(first_owned)
# if you are unsure whether to use the del statement or the pop method, a simple way to decide;
# when you want to delete an item from a list and not use the item in any way, use the del statement;
# if you want to use an item from a list as you remove it, use the pop() method.
too_expensive = 'honda' # removing an item by value; this case is where you don't know the position, 
# of a value in the list.
# the remove() method deletes only the first occurrence of the value you specify; if there is a,
# possibility the value appears more than once, you will need to use a loop to make sure all,
# occurences of the value are removed. 
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"A {too_expensive.upper()} is too expensive for me")
# organizing a list 
cars = ['toyota', 'bmw', 'audi', 'subaru']
cars.sort() # sorting a list permanently with the sort() method
print(cars) 
print("Here is the original list:")
print(cars)
print("Here is the sorted list:")
print(sorted(cars)) # sorting a list temporarily with the sorted() method
print("Here is the original list again:")
print(cars)
cars.reverse() # printing a list in reverse order
print(cars)
len(cars) # printing the length of a list using len()

# looping through a list; looping allows you to take the same actio, or set of actions, 
# with every item in a list, set of steps repeated for every item in a list 
magicians = ['alice','david','segun']
for magician in magicians:
    print(magician.title()) 
    print(f"{magician.title()}, that was a great trick!\n")
# \n at the end of the string leaves a blank line after the loop on each item list
# Doing something after a loop, the line below is indented, so it's not in the loop code
print("Thank you everyone, That was a great magic show!") 

# making numerical lists 
for value in range(1,5):
    print(value)
for value in range(1,6):
    print(value)
# Using range() to make a list of numbers 
numbers = list(range(1,6))
print(numbers)
even_numbers = list(range(2,11,2))
print(even_numbers)
squares = []
for value in range(1,5):
    square = value ** 2
    squares.append(square)
print(squares) 
# simple statistics for a list of numbers, min, max, sum, pow
digits = [1, 2, 3, 4, 5]
ner = min(digits)
print(ner) 
mer = max(digits)
print(mer)
xer = sum(digits)
print(xer)
ger = pow(digits[0], digits[4])
print(ger)
# sicing a list 
players = ['juwon', 'sane', 'fasan', 'laitan']
print(players[0:3])
print(players[1:2])
print(players[:3]) 
print(players[1:])
print(players[-3:])
# Looping through a sliced list 
print("\nHere are the first three players of the team: ")
for player in players[:3]:
    print(player.title())
# Copying a list; using :, =
foods = ['cake', 'pizza', 'malt']
fav_foods = foods[:]
print(fav_foods)
foods.append('sharwama')
print(foods)
fav_foods.append('sugar')
print(fav_foods)
fav_foods = foods # this syntax tells Python to associate the elements in both lists
foods.append('malta')
print(fav_foods)
print(foods) 

# Tuples; a list of items that is immutable; items can't be changed or modified throughout the life of a program
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# Looping through values in a tuple
for dimension in dimensions:
    print(dimension)
print("\nOriginal documents:")
for dimension in dimensions:
    print(dimension) 
dimensions = (400, 100)
print("\nModified documents:")
for dimension in dimensions:
    print(dimension)

# Sytle Guide: Indentation(Tab, Space), Line Length(79-99 character limit), Blank Lines 

# if statement: statement examining a set of conditional tests and which action to take,
# based on those conditional tests.
cars = ['audi', 'bmw', 'toyota', 'subaru']
for car in cars: 
    if car == 'bmw': # conditional tests:==, checks whether a variable is indeed equal to its value, checking for equality                    
        print(car.upper())
    else:
        print(car.title())
requested_topping = 'mushrooms'
if requested_topping != 'anchovies': # conditional tests; checking for inequality, no need for else statement
    print("Hold the anchovies!")

#if - else statement
surname = 'sala'
firstname = 'muja'
if surname == 'sala' and firstname == 'muja':
    print("True")
else:
    print("False")
if surname == 'sala' or firstname == 'muja':
    print("False")
else:
    print("True") 
#if - else statement
nightouts = ['cruzer', 'kokobean', 'sluggers']
nightout1 = 'sluggers'
nightout2 = 'house25'
#if - elif - else statement
age = 50
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else: 
    price = 20
print(f"Your admission cost is ${price}.")

# testing multiple conditions, multiple if statements 
if nightout1 in nightouts: # checking whether a value is in a list 
    print("True")
else:
    print("False")
if nightout2 not in nightouts: # checking whether a value is not in a list 
    print("True")
else:
    print("False")
#if - else statement
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?") # use input fctn
else:
    print("You are too young to vote!")
    print("Please register to vote as soon as you turn 18!")

# Using if statements with lists 
toppings = ['mushrooms', 'pepperoni', 'cheese']
for topping in toppings:
    if topping == 'cheese':
        print("We are out of cheese right now.")
    else:
        print(f"Adding {topping}.")
print("\nHere is your pizza!")

# Dictionaries; a collection of key-value pairs--key is connected to a value, 
# and you can use a key to access the value associated with that key 
alien_0 = {
    'color':'green', 
    'points': 5
}
# Accessing values in a dictionary
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print(f"You just earned {new_points} points!")
alien_0['x-postion'] = 0 
alien_0['y-postion'] = 25
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)
print(f"The alien colour is now {alien_0['color']}")  
del alien_0['points']
print(alien_0)
alien_1 = {
    'x-position': 0, 
    'y-position': 2, 
    'speed': 'medium'
}
print(f"Original x-postion: {alien_1['x-position']}")
print(f"Original y-postion: {alien_1['y-position']}")  
# modifying values in a dictionary
if alien_1['speed'] == 'slow':
    x_increment = 1
    y_increment = 3
elif alien_1['speed'] == 'medium':
    x_increment = 2
    y_increment = 5
else:
    # This must be a fast alien
    x_increment = 3
    y_increment = 7
# The new position is the old position plus the increment.
alien_1['x-position'] = alien_1['x-position'] + x_increment
alien_1['y-position'] = alien_1['y-position'] + y_increment
print(f"New x-position: {alien_1['x-position']}")
print(f"New y-position: {alien_1['y-position']}")
# Looping through a dictionary 
for position, value in alien_1.items(): # looping through key-value pairs
    print(f"\nPosition: {position}")
    print(f"Value: {value}")
for position in alien_1.keys(): # looping through keys 
    print(position) 
for value in alien_1.values(): # looping through values
    print(value) 
coordinates = ['x-position', 'y-position', 'z-position']
for position in alien_1.keys():
    print(position.title()) 
    if position in coordinates:
        value = alien_1[position]
        print(f"\t{position.title()}, I see your position {value}!") 
# nesting; a dictionary in a list
eats_ibadan = {
    'bistro': 'west grill', 
    'mall': 'queencinema',
}
eats_lagos = {
    'bistro': 'undgerground', 
    'mall': 'icm',
} 
eats = [eats_ibadan, eats_lagos]
for eat in eats:
    print(eat)
# nesting; a dictionary in a list
aliens = []
# Make 30 green aliens.
for alien in range(30):
    alien = {
        'color': 'green', 
        'points': 5, 
        'speed': 'slow',
}
    aliens.append(alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'
# Show the first 5 aliens.
for alien in aliens[:5]: 
    print(alien)
print("...")
# Show the total number of aliens
print(f"The total number of aliens:{len(aliens)}")
print(aliens)

# nesting; list in a dictionary
pizza = {
    'crust': 'thick', 
    'toppings':['mushrooms', 'extra cheese'], 
    'shape': 'circle',
}
print(f"\nYou ordered a {pizza['shape']} {pizza['crust']} pizza with the following toppings:")
for topping in pizza['toppings']: 
    print(topping)
# nesting; lists in a dictionary
fav_langs = {
    'jen': ['python', 'ruby'], 
    'sarah': ['C'], 
    'edward': ['ruby', 'go'], 
    'phil': ['python', 'haskell'],
}
for name, langs in fav_langs.items(): 
    print(f"\n{name.title()}'s favourite languages are:")
    for lang in langs:
        print(lang.title()) 

#nesting; a dictionary in a dictionary
student_details = {
    'tm': {
        'first': 'tomiwa',
        'last': 'aribisala',
        'location': 'lagos',
        },
    'rayo': {
        'first': 'tunrayo',
        'last': 'deji',
        'location': 'ibadan',
        },
    'ifey': {
        'first': 'ife',
        'last': 'petu',
        'location': 'ekiti', 
        },
}
for username, user_info in student_details.items():
    print(f"\nUsername: {username}")
    print(f"\tFirst Name: {user_info['first']}")
    print(f"\tLast Name: {user_info['last']}")
    print(f"\tLocation: {user_info['location']}") 
# you should not nest lists and dictionaries too deeply, If you’re nesting items much 
# deeper than what you see in the above examples or you’re working with someone 
# else’s code with significant levels of nesting, most likely a simpler way to solve the 
# problem exists.
# all of the dictionaries or dictionary in a dictionary in a list should have identical structure,
# so you can loop through the list or dictionary and work with the dictionary/list object in the 
# same way or vice versa

# functions; blocks of code designed to do a specific job
def greet_user(username): # function name
    """Display a simple greeting.""" # docstring; this line describes the action the function performs
    print(f"Hello, {username.title()}")
greet_user('sarah')

# passing arguments; positional arguments, keyword arguments, default values 
def describe_pet(animal_type, pet_name):
    """"Display info about a pet"""
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")
describe_pet('hamster', 'harry') # positional argument
describe_pet('dog', 'willie') # positional argument 
describe_pet(pet_name='billy', animal_type='cat') # keyword argument 

def ibadan_eats(restaurant, location='bodija'): # default value
# when you use default values, any parameter with a default value needs to,
# be listed after all the parameters that don't have default values.
    """Display restaurants in Ibadan"""
    print(f"I love the food at {restaurant} in {location}. ")
ibadan_eats(restaurant='west grill')
ibadan_eats(restaurant='west grill', location='moniya') # in this argument the location parameter described,
# is not 'bodija'(different from the parameter default value), 
# this argument can be specified using positional or default argument

# return value: returns a value calling a function, note that you should not 
# write any code after the return value, the return value closes the function
def get_formatted_name(first_name, last_name):
    """Display a neatly formatted name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician) 
painter = get_formatted_name('jesse', 'sutton')
print(painter) 
bricklayer = get_formatted_name('jeff', 'jerome')
print(bricklayer) 

# return value, making an argument optional--middle name 
def get_adjusted_name(first_name, last_name, middle_name=''):
    """Display a neatly adjusted name"""
    if middle_name: 
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_adjusted_name('jimi', 'hendrix')
print(musician) 
painter = get_adjusted_name('jesse', 'sutton', 'daniel')
print(painter) 

# return value, returning a dictionary
def build_person(first_name, last_name, age=''):
    """Return a dictionary about a person information"""
    if age:
        person = {
            'first': first_name, 
            'last': last_name, 
            'age': age
        }
    else:
        person = {
            'first': first_name, 
            'last': last_name
        }
    return person
salaa = build_person('tomiwa', 'arib', '27')
print(salaa)

# using a function with a while loop 
def formatted_name(f_name, l_name): 
    """Return a neatly, formatted name."""
    fu_name = f"{f_name} {l_name}"
    return fu_name
while True: # using a flag
    print("Enter your name:")
    print("enter 'q' at any point to quit")
    fi_name = input("First name: ")
    if fi_name == 'q': 
        break
    la_name = input("Last name: ")
    if la_name == 'q': 
        break
neat_formatted_name = formatted_name(fi_name, la_name)
print(f"\nHello, {fi_name} {la_name}!")

# function, passing a list 
def greet_users(names): 
    """Print a simple greeting to a list of users"""
    for name in names: 
        print(f"Hello, {name.title()}!")
usernames = ['ken', 'karen', 'kenneth']
greet_users(usernames) 

# modifying a list in a function
unprinted_designs = ['phone case', 'robot', 'pendant']
completed_models = []
def print_models(unprinted_designs, completed_models): 
    """Simulate printing each design, until none are left
    Move each design to completed_designs after printing 
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """Show all the models that are printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model) 
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models) 

# passing an arbitrary number of arguments in a function, *args
def make_pizza(size, *toppings): # the parameter that accepts an arbitrary number of arguments, 
                                 # must be placed LAST in the function definition
    """Summarize the pizza we are about to make"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
make_pizza(16, 'pepperoni')
make_pizza(17, 'debonair', 'cheese')

# using arbitrary keyword arguments via a dictionary, **kwargs
def build_profile(first, last, **user_info):
    """Build a dictionary about everything we know about a user"""
    user_info['first_name'] = first 
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile) 


# Classes; Object Oriented Programming; write classes--code that represents, 
# real world things and situations, and you create objects based on those classes, 
# When you write a class, you define the general behaviour that a whole category  
# of objects can have. 
class Dog: # by convention, classes names start with upper case
    """A simple attempt to model a dog."""

    def __init__(self, name, age): # the default init method--function, self parameter is 
                                    # required in this method definition, and it must come,
                                    # before other parameters
        """Initialize name and age attributes."""
        self.name = name    
        self.age = age 
    # Any variable prefixed with self is available to every method in the class, 
    # and we’ll also be able to access these variables through any instance created from the class. 
    # Variables that are accessible through instances like this are called attributes.
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
        print(f"{self.name} is over {self.age} years old.")

# making an instance from a class; multiple instances
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}, he is {my_dog.age} years old.") # accessing attributes
your_dog = Dog('Lucy', 3)
print(f"My dog is {your_dog.age} years old, his name is {your_dog.name}.") # accessing attributes
my_dog.sit() # calling methods
your_dog.roll_over() # calling methods

# working with classes and instances
class Car: 
    """A simple statement to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year 
        self.odometer_reading = 23 # setting a default value for odometer_reading attribute
                                   # Attributes can be defined without being passed in as, 
                                   # parameters, these can attributes can be defined in the init method.
    def get_descriptive_name(self): 
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Return a car odometer number."""
        sup_name = f"My old car has {self.odometer_reading} miles on it!"
        return sup_name.title()

    def update_odometer(self, mileage):  # modifying an attribute value through a method 
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage

my_old_car = Car('toyota', 'camry', 2010)
print(my_old_car.get_descriptive_name())
print(my_old_car.read_odometer())
my_new_car = Car('toyota', 'muzzle', 2020)
my_new_car.update_odometer(44) # modifying an attribute value through a method 
print(my_new_car.read_odometer())
print(f"The {my_new_car.year} {my_new_car.make} is parked at Afrikan Lane.") # accessing attributes 

# inheritance; original class--parent class and new class--child class;
# The child class inherits the attributes and methods of its parent class, 
# but it’s also free to define new attributes and methods
class ElectricCar(Car): # when you write a child class, the parent class, 
                        # must be part of the current file and must appear, 
                        # after the child class in the file.
    """Represent aspects of a electric car"""

    def __init__(self, make, model, year): # the init method
        """Intialize attributes of the parent class
        Then initialize attributes specific to a electric car"""
        super().__init__(make, model, year) # this super() function is a special function that allows, 
                                            # you to call a method from the parent class
                                            # This line tells Python to call the __init__() method from Car
                                            # which gives an ElectricCar instance all the attributes 
                                            # defined in the init method.
        # self.battery_size = 75 # This attribute will be associated with all instances created from, 
                                 # the ElectricCar but won't be associated with any instances of Car.
        # def describe_battery(self):
        # """Print a statement describing the battery size."""
        # print(f"This car has a {self.battery_size}-kWh battery.")
        self.battery = Battery() # instances as atrributes 

class Battery: # instances as attributes 
    """A simple battery case of an electric car"""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size 

    def describe_battery(self):
        """Return the battery size of an electric car"""
        bat_size = f"This car has a {self.battery_size} Kwh capacity."
        return bat_size 
    
    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 75:
            range = 260 
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.")

my_telsa = ElectricCar('dodge', 'challenger', 2015) # testing inheritance
print(my_telsa.get_descriptive_name()) # testing inheritance
print(my_telsa.battery.describe_battery())
my_telsa.battery.get_range()

# the python standard library 


# files; open(), close()
filename = 'pi_digits.txt'
with open(filename, 'r') as file_object: # calling open() to open the file,
                                    # the keyword with closes the file once it is non longer needed.
    contents = file_object.read() # reading a file
    print(contents.rstrip()) # using rstrip() to remove whitespace

file_name = 'programming.txt'
with open(file_name, 'w') as file_prog:
    file_prog.write("I love programming.") # writing to a file
    file_prog.write("\nI love creating new games.") # writing to a file
# Be careful before opening a file in write mode('w'), if the file does exist, 
# python will erase the content of the file before returning the file.
# python can only write strings to a text file. If you want to store numerical data in a 
# text file, you’ll have to convert the data to string format first using the str() function
with open(file_name, 'a') as file_sum: # appending to a file 
    file_sum.write("\nBurna Boy has an expansive sonic palette.") # writing, appending to a file
    file_sum.write("\nI consider Wizkid as the greatest artist of his generation.") # writing, appending to a file

# reading a file line by line; line
# making a list of lines from a file; readlines 

# exceptions; manage errors during a program's execution, try-except code blocks, else block

# storing data; using JSON
import json
numbers = [2, 3, 4, 5, 7, 16]
file = 'numbers.json'
with open(file, 'w') as f: # writing to a file, the numbers.json does not contain any data earlier 
    json.dump(numbers, f) # using json.dump; storing numbers into the file numbers.json file
                            # json.dump takes two arguments; a piece of data to store and 
                            # a file object it can use to store the data.
file = 'numbers.json'
with open(file, 'r') as f:
    numbers = json.load(f) # using json.load; reading numbers.json file back to memory
print(numbers)

# saving user-generated data
import json 
username = input("What is your name? ")
file_p = 'username.json' 
with open(file_p, 'w') as f:
    json.dump(username, f)
    print(f"We will remember you when you come back,{username}") 

# reading user-generated data
import json 
with open(file_p, 'r') as f:
    username = json.load(f) 
    print(f"Welcome back, {username}")

# Testing your code; testing a function--see name_function.py and testing_clean_name_function.py files
def get_clean_name(first, last, middle=''): 
    """Generate a clean name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else: 
        full_name = f"{first} {last}"
    return full_name.title()

# testing methods in a class; see anonymous_survey_function.py and testing_anonymous_survey_Class files
class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""
    def __init__(self, question): 
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response): 
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses given."""
        print("Survey results:")
        for response in self.responses:
            print(f"-{response}")