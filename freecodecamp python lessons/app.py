print("Hello World") # print

character_name = 'John' # variable
character_age = 35 # variable
print(f"My name is {character_name},") # use of f-string
print(f"and i am {character_age} years old.")  # use of f-string

character_name = 'Tomiwa' # variable
character_age = 25 # variable
print(f"\nMy name is {character_name},")  # use of f-string and new line
print(f"and i am {character_age} years old.")  # use of f-string

phrase = "Giraffe Academy" # variable
print(f"\n{phrase} is cool")  # use of f-string and new line
print(phrase.lower()) # lower case 
print(phrase.upper()) # upper case 
print(phrase.title()) # first letters upper case
print(len(phrase)) # variable length
print(phrase[0]) # variable indexing
print(phrase[3]) # variable indexing 
print(phrase.index('i')) # variable index
print(phrase.replace('Giraffe', 'Decagon')) # variable replace fctn 

print(abs(-5)) # absolute value fctn
print(pow(4, 2)) # This line means 4 raised to the power of 2--4**2
print(max(1, 2)) # maximum value fctn
print(min(1, 2)) # minimum value fctn
 
friends = ['isaiah', 'juwon', 'sola', 'isaiah', 'jade',] # lists, can contain strings, 
# numbers and booleans(true/false)
friends[0] = 'mike'
print(friends[0]) # list indexing
print(friends[-1]) # list indexing
print(friends[1:]) # list indexing
print(friends[1:3]) # list indexing
friends.insert(5, 'pamilerin')
print(friends) 
# basic list fctns: extend(), insert(index, ''), append(''), remove(''), clear(), pop(), count(''), 
# index(''), sort(), reserve()

# tuples: container of values, immutable, values can be accessed but can't be modified or changed
coordinates = (4,5)
co_ordinates = [(4,5), (6,7), (5,10)] # tuples contained in a list 
print(coordinates[1]) 

# functions: features---lowercase, underscore, indentation
def say_hi(name, age):
    print(f"\nHello {name}, you are {age}")
say_hi(name = 'Nonso', age = 55) # calling the function 

# return value: returns a value calling a function, note that you should not 
# write any code after the return value, the return value closes the function
def cube(num):
    return num**2
result = cube(3) # calling the function 
print(result)

# if statements: statements to check if conditions are true/false, we give certain results, 
# else we check other conditions, and(joiner), or(joiner)
tall_male = 13 # inches 
short_male = 5 # inches 
if tall_male == 13 and short_male == 5:
    print("You and your brother meet the specified heights.")
elif tall_male == 13 and short_male != 5:
    print("The older brother meet the specified height.")
elif tall_male != 13 and short_male == 5:
    print("The younger brother meet the specified height.")
else:
    print("The heights stated do not meet the industry criteria.")
# if statements and comparisons: <, >, <=, >=,!=
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3: 
        return num1
    elif num1 <= num2 and num1 <= num3: 
        return num2 
    else: 
        return num3
mode = max_num(3, 4, 5) # calling the function 
print(mode)

# Dictionaries: storing key-value pairs 
monthConversions = { 
    'jan': 'january',
    'feb': 'february',
    'mar': 'march',
    'apr': 'april'
}
print(monthConversions['jan']) 

# while loop: looping through a block of code multiple times in respect to a stated condition,
# python checks the defined variables, then check the while loop condition for the defined variables,
# then python loops through the while loop code, in respect to the stated condition, this action 
# repeats itself again and again unil the loop code is completeted---in respect to the stated condition.
i = 1
while i <= 10: 
    print(i)
    i += 1

# for loop: looping through different collection of items; strings, numbers, series, arrays, lists 
friends = ['sam', 'tomiwa', 'seun']
for  friend in friends:
    print(friend)
for index in range(3):
    if index == 0:
        print('first iteration')
    else:
        print('exception')

# exponent fctn example 
def raise_to_power(base_num, pow_num):
    for index in range(pow_num):
        result = 1*base_num
    return result
exponent = raise_to_power(3,2)
print(exponent)

# 2D Lists: lists contained in a list, written in grid-structure--rows/columns,
# index of rows/columns starts from 0.
number_grid = [
    [0],
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(number_grid[2][1])
# Nested Loops
for row in number_grid:
    for col in row: 
        print(col)

# Comments: statements starting with # to describe code blocks, python does not process comments

# Try/Except Concept; 

# Reading files: opening and closing text files in the same directory, 
# modes: read--r, write--w, append--a, read/write--r+ to a file---text file 
employee_file = open('employeesfile.txt', 'w')
employee_file.write('Toby - Human Resources')
employee_file = open('employeesfile.txt', 'r')
print(employee_file.readlines())
# Appending to files,
employee_file = open('employeesfile.txt', 'a') 
employee_file.write('Jim - Salesman')
employee_file.close
# Writing to files, note that using the write--w mode overwrites the whole file entirely
employee1_file = open('employees1.txt', 'w')
employee1_file.write('Kelly - Customer Service')
employee1_file.close 
employee1_file = open('employees1.txt', 'a')
employee1_file.write('\nDanny - Logistics')
employee1_file.close 


# Modules and Pip: modules--files for storing functions, you can import modules,
# calling functions in modules to other files, pip is for python external modules installation--python docx 

# Classes and objects: OOP, storing real life objects in python, check student.py file 

# Inheritance: class and sub-class: sub-class inherits main class functions and attributes,
# check student.py file

