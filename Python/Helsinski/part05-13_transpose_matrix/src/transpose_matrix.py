# Write your solution here
def transpose(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            list[i][j], list[j][i] = list[j][i], list[i][j]
    

if __name__ == "__main__":
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    transpose(matrix)
    print(matrix)