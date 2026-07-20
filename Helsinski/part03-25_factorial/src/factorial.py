# Write your solution here
while True:
    num = int(input("Please type in a number: "))
    if num <= 0:
        break
    i = 0
    sumy = 1
    while i < num:
        i += 1
        sumy *= i  
    print(f"The factorial of the number {num} is {sumy}")
print("Thanks and bye!")