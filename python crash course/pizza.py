# THis file is a module, 
# A module is a file ending in .py that contains the code you want,
# to import into your program, we remove everything else from the module, 
# except the function 


# # passing an arbitrary number of arguments in a function, *args
def make_pizza(size, *toppings): # the parameter that accepts an arbitrary number of arguments, 
                                 # must be placed LAST in the function definition
    """Summarize the pizza we are about to make"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

# return value, returning a dictionary
def build_person(first_name, last_name, age=''):
    """Return a dictionary about a person information"""
    if age:
        person = {'first': first_name, 'last': last_name, 'age': age}
    else:
        person = {'first': first_name, 'last': last_name}
    return person