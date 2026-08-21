# Write your solution here# Write your solution here
import string
import random

def generate_strong_password(amount, condition1, condition2):
    password = ""
    pool = string.ascii_lowercase
    if condition1:
        pool += string.digits
        password += random.choice(string.digits)
    if condition2:
        pool += "!?=+-()#"
        password += random.choice("!?=+-()#")
    for i in range(amount - len(password)):
        password += random.choice(pool)
    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))