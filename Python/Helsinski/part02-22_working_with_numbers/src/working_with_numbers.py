# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
counter = 0
summar = 0
posit = 0
neg = 0
while True:
    num = int(input("Number: "))
    if num == 0:
        break
    if num >= 0:
        posit += 1
    else:
        neg += 1
    counter += 1
    summar += num

print(f"Numbers typed in {counter}")
print(f"The sum of the numbers is {summar}")
print(f"The mean of the numbers is {summar/counter}")
print(f"Positive numbers {posit}")
print(f"Negative numbers {neg}")
