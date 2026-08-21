# Write your solution here
from random import randint
def lottery_numbers(amount, lower, upper):
    winner = []
    while len(winner) < amount:
        new = randint(lower, upper)
        if new not in winner:
            winner.append(new)
    return sorted(winner)

if __name__ == "__main__":
    for number in lottery_numbers(7,1,40):
        print(number)