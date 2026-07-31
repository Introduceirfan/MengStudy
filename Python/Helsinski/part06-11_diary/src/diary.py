# Write your solution here
def diary():
    while True:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        input_func = int(input("Function: "))

        if input_func == 1:
            diary_input = input("Diary entry: ")
            with open("diary.txt", "a") as my_file:
                my_file.write(f"{diary_input}\n")
            print("Diary saved")

        elif input_func == 2:
            print("Entries: ")
            with open("diary.txt", "r") as new_file:
                for line in new_file:
                    parts = line.strip()
                    print(parts)
        else:
            print("Bye now!")
            break
diary()