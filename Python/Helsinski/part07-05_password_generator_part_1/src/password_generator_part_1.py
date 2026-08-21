# Write your solution here
import string
import random

def generate_password(amount):
    char = string.ascii_letters
    password = ""
    for i in range(amount):
        password += random.choice(char)

    return password.lower()
if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))