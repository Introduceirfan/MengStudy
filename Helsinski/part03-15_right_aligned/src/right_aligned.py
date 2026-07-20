# Write your solution here
string = str(input("Please type in a string: "))
star = "*"
if len(string) < 20:
    print((star * (20 - len(string)) + string))