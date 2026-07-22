# Write your solution here
def all_the_longest(list):
    best = len(list[1])
    new_list = []
    for i in list:
        if len(i) > best:
            best = len(i)
            new_list = [i]
        elif len(i) == best:
            new_list.append(i)
    return new_list

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['eleventh']