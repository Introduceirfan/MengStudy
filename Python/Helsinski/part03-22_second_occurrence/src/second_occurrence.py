string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

first_occurrence = string.find(substring)

if first_occurrence != -1:
    second_occurrence = string.find(substring, first_occurrence + len(substring))
    if second_occurrence != -1:
        print(f"The second occurrence of the substring is at index {second_occurrence}.")
    else:
        print("The substring does not occur twice in the string.")
else:
        print("The substring does not occur twice in the string.")