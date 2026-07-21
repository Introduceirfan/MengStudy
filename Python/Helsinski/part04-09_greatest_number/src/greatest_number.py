# Write your solution here
def greatest_number(x1,x2,x3):
    if x1 >= x2 and x1 >= x3 :
        return x1
    if x2 >= x1 and x2 >= x3 :
        return x2
    else:
        return x3
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(3,5,7)
    print(greatest)