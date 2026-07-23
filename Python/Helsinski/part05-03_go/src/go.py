# Write your solution here
def who_won(list):
    count1 = 0
    count2 = 0
    for i in list:
        for j in i:
            if j == 1:
                count1 += 1
            elif j == 2:
                count2 += 1
    if count1 > count2:
        return 1
    elif count2 > count1:
        return 2
    else:
        return 0
if __name__ == "__main__":
    board = [
    [1, 0, 2],
    [1, 1, 0],
    [2, 2, 0]]

    print(who_won(board))