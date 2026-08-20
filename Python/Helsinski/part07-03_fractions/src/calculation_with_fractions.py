# Write your solution here
from fractions import Fraction
def fractionate (amount: int):
    part = Fraction(1, amount)
    return [part] * amount

if __name__ == "__main__":
    for p in fractionate(3):
        print(p)