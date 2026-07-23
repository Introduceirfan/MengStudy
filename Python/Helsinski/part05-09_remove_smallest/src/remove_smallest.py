# Write your solution here
def remove_smallest(list):
    lowest = list[0]
    for i in list:
        if i < lowest:
            lowest = i
    list.remove(lowest)

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)