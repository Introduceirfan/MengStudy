# Write your solution here
while True:
    string = str(input("Please type in a string: "))
    if len(string) == 0:
        break
    line = "-"
    print(string)
    print(line * len(string))