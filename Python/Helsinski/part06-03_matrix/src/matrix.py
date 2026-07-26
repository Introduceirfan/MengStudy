# write your solution here
def read_matrix():
    with open("matrix.txt") as new_file:
        matrix_list = []
        for line in new_file:
            parts = line.split(",")
            matrix_list.append(parts)
        return matrix_list

def matrix_sum():
    matrix = read_matrix()
    sum = 0
    for row in matrix:
        sum += row
    return matrix 
    
if __name__ == "__main__":
    
    print(read_matrix())