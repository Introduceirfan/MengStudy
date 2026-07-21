# Write your solution here
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
op = input("Operation: ")
if op == "add":
    add = num1 + num2
    print(f"{num1} + {num2} = {add}")
if op == "multiply":
    mulp = num1 * num2
    print(f"{num1} * {num2} = {mulp}")
if op == "subtract":
    subt = num1 - num2
    print(f"{num1} - {num2} = {subt}")
