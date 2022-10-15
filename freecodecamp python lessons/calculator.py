# use of input and float fctns to build a calculator 

num1 = float(input("Enter a first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter a second number: "))
# float and int are python functions to convert user input to numerical format 
if op == '+':
    add = num1 + num2
    print(add) 
elif op == '-':
    subtract = num1 - num2
    print(subtract)
elif op == '*':
    multiply = num1*num2
    print(multiply)
elif op == '/':
    divide = num1/num2
    print(divide)
else:
    print("Invalid operator")