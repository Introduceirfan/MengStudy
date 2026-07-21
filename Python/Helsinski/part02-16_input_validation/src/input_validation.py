from math import sqrt
# Write your solution here
while True:
    number = int(input("Please type in a number: "))
    if number == 0:
        break
    if number < 0:
        print("Invalid number")
    if number > 0:
        print(f"{sqrt(number)}")
print("Exiting...")