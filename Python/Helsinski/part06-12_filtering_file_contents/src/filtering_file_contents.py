# Write your solution here
def filter_solution():
    with open('solutions.csv', 'r') as new_file:
        for line in new_file:
            parts = line.split(";")
            result[parts[0]] = []
            for res in parts:



if __name__ == "__main__":
    filter_solution()