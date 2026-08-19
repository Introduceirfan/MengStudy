# Write your solution here
import random

def lottery_numbers(amount: int, lower: int, upper: int) -> list:
    numbers = []
    while len(numbers) < amount:
        random_num = random.randint(lower, upper)
        if random_num not in numbers:
            numbers.append(random_num)
    numbers.sort()
    
    return numbers
for number in lottery_numbers(7, 1, 40):
    print(number)