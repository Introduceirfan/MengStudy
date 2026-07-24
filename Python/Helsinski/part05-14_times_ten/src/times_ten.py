# Write your solution here
def times_ten(x, y):
    dict = {}
    for i in range (x, y +1):
        dict[i] = i * 10
    return dict
if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)