# Modifying a dictionary; filling a dictionary with user input
responses = {

}
# Set a flag that polling is active
polling_active = True # Using a flag
while polling_active:
    # Prompt for person's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    # Store the response in a dictionary
    responses[name] = response 
    # repeat if anyone else is taking the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
        break # Using break to exit a loop
# Polling is complete, show the results 
print("\n---Poll Results---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}")

def get_adjusted_name(first_name, last_name, middle_name='', nick_name=''):
    """Display a neatly adjusted name"""
    if middle_name: 
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    if nick_name:
        full_name = f"{first_name} {middle_name} {last_name} {nick_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_adjusted_name('jimi', 'hendrix')
print(musician) 
painter = get_adjusted_name('jesse', 'sutton', 'daniel')
print(painter) 
bricklayer = get_adjusted_name('jeff', 'jerome', 'hooker', 'lee')
print(bricklayer) 
