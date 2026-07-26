# write your solution here
def read_fruits():
    with open("fruits.csv") as new_file:
        fruits_list = {}
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            fruits_list[parts[0]] = float(parts[1])
        return fruits_list
if __name__ == "__main__":
    print(read_fruits())