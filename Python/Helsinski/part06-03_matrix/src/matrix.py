# write your solution here
def read_matrix():
    with open("matrix.txt") as new_file:
        matrix_list = []
        for line in new_file:
            parts = line.strip().split(",")
            row = []
            for matrax in parts:
                row.append(int(matrax))
            matrix_list.append(row)
        return matrix_list

def matrix_sum():
    matrix = read_matrix()
    list_sum = []
    for row in matrix:
        list_sum.append(sum(row))
    return sum(list_sum) 

def matrix_max():
    matrix = read_matrix()
    list_max = []
    for row in matrix:
        list_max.append(max(row))
    return max(list_max)

def row_sums():
    matrix = read_matrix()
    list_row_sum = []
    for row in matrix:
        list_row_sum.append(sum(row))
    return list_row_sum

if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())