# Write your solution here
number = int(input("Please type in a number: "))
i = 1
j = number
while i*2 <= number:
    print (i)
    print (j)
    i += 1
    j -= 1
if number % 2 != 0:
    print(i)