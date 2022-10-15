from hello import get_clean_name 

print("Enter 'q' at any point to quit")
while True:
    first = input("\nPlease give your first name: ")
    if first == 'q':
        break
    last = input("Please give a last name: ")
    if last == 'q': 
        break 
    formatted_name = get_clean_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.") 
