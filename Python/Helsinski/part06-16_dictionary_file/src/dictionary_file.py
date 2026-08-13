# Write your solution here
def dictionary():
    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        funct = int(input("Function: "))
        if funct == 1:
            word = str(input("The word in Finnish: "))
            translate = str(input("The word in English:"))
            with open("dictionary.txt", "a") as new_file:
                new_file.write(f"{word}:{translate}\n")
                print("Dictionary entry added")

        elif funct == 2:
            search = str(input("Search term: "))
            with open("dictionary.txt", "r") as new_file:
                for line in new_file:
                    parts = line.strip().split(":")
                    if search in parts[0] or search in parts[1]:
                        print(f"{parts[0]} - {parts[1]}")

        elif funct == 3:
            print("Bye!")
            break


dictionary()