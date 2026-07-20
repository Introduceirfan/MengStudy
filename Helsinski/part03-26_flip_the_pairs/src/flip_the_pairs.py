# Write your solution here
number = int(input("Please type in a number: "))
i = 1
while i <= number:
    if i % 2 != 0:
        if i == number:
            print(number)
        else:
            print(i + 1)
    if i % 2 == 0:
        print(i-1)
    i += 1