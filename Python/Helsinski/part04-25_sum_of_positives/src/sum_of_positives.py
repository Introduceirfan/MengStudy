# Write your solution here
def sum_of_positives(list):
    new_list = []
    for i in list:
        if i >= 0:
            new_list.append(i)
    return sum(new_list)

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)