# Write your solution here
def create_tuple(x,y,z):
    small = min(x,y,z)
    maxim = max(x,y,z)
    sumi = x + y + z

    return (small, maxim, sumi)
if __name__ == "__main__":
    print(create_tuple(5, 3, -1))