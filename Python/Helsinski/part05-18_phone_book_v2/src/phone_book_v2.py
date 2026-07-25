# Write your solution here
dict = {}
while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 1:
        name = input("name: ")
        if name in dict:
            for number in dict[name]:
                print(number)
        else:
            print("no number")

    if command == 2:
        add_name = input("name: ")
        add_num = input("number: ")
        if add_name not in dict:
            dict[add_name] = []
        dict[add_name].append(add_num)
        print("ok!")

    if command == 3:
        print("quitting...")
        break
