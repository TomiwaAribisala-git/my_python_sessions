# User input()--using input fctn;
name = input("Please enter your first name: ")
print(f"Hello,{name.title()}!") 

# Building a multi-line string, using input() fctn:
prompt = "Tell us who you are"
prompt += "\nWhat is your first name? "
fname = input(prompt)
print(f"Hello,{fname.title()}!")

# Using int(), input() to accept numerical input:
height = int(input("How tall are you, in inches? "))
if height >= 48:
    print("\nYou are tall enough to ride.")
else:
    print("\nYou will be able to ride when you are a little older.")
    
# Modulo Operator: %, int(), input()
number = int(input("Enter your number, I will tell you if it's even or odd: "))
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd")

# while loop: runs as long as, or while condition is true
current_number = 1 
while current_number <= 5: 
    print(current_number)
    current_number += 1
# Using a flag; for a program that should run only as many conditions are true, 
# you can define one variable, that determines whether or not the program is active,
# the variable, called a flag, acts as a signal to the problem. 
fav_fruit = "Tell us your favourite fruit: "
fav_fruit += "Enter 'quit' to exit the fruit program. "
active = True 
while active:
    message = input(fav_fruit)
    if message == 'quit':
        active = False 
    else: 
        print(message) 
# Using break to exit a loop:
fav_city = "Tell us a city you once visited: "
fav_city += "Enter 'quit' to exit the city program. "
while True: # using a flag 
    city = input(fav_city)
    if city == 'quit': 
        break 
    else: 
        print(f"I would love to go to {city.title()}")
# Using continue in a loop: 
axis_number = 0
while axis_number < 10:
    axis_number += 1 
    if axis_number % 2 == 0:
        continue
    print(axis_number) 
#Using a while loop with lists and dictionaries:
# A for loop is effective for looping through a list, but you shouldn’t modify 
# a list inside a for loop because Python will have trouble keeping track of the 
# items in the list. To modify a list as you work through it, use a while loop. 
# Using while loops with lists and dictionaries allows you to collect, store, and 
# organize lots of input to examine and report on later. 
unconfirmed_users = ['alice', 'brian', 'candance']
confirmed_users = []
# Verify each user so that there are no more unconfirmed users, 
# Move each user to the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}") 
    confirmed_users.append(current_user)
print(confirmed_users) 
# Display confirmed users
print(f"The following users has been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
# Modifying a list using while loop; Removing Instances of Specific Values in a list
pets = ['dog', 'cat', 'mouse', 'snake', 'cat']
print(pets)
while 'cat' in pets: 
    pets.remove('cat')
print(pets)

