# Write your solution here
def most_common_character(string):
    count = 0
    most_string = string[0]
    for i in string:
        counting = string.count(i)
        if counting > count:
            count = counting
            most_string = i
    return most_string

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))