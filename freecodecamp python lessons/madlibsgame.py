# use of variable, input, and f-string to build a mad-libs-game 

first_name = input("Please enter your first name: ")
age = input("Enter your age: ")
print(f"Hi {first_name}, your age is {age}")

color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print(f"Roses are {color}")
print(f"{plural_noun.title()} are blue")
print(f"I love {celebrity}") 