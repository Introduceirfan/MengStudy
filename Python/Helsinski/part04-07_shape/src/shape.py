# Copy here code of line function from previous exercise and use it in your solution
def line(num, x):
    if x == "":
        print(num * "*")
    else:
        print(num * x[0])

def shape(width, x1, height, x2):
    i = 1
    j = 1
    while i <= width:
        line(i, x1)
        i += 1
    while j <= height:
        line(width, x2)
        j += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")