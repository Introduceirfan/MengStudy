# Write your solution here
string = str(input("Please type in a string: "))
tes = len(string)
sane = 0
while sane <= tes:
    print(string[tes:])
    tes -= 1