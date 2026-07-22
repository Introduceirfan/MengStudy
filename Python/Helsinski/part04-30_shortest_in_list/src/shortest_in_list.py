# Write your solution here
def shortest(list):
    short = list[1]
    for i in list:
        if len(i) < len(short):
            short = i 
    return short
if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = shortest(my_list)
    print(result)