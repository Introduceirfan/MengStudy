# Write your solution here
def invert(dictionary):
    list1 = list(dictionary.items())
    dictionary.clear()
    for key, value in list1:
        dictionary[value] = key

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)