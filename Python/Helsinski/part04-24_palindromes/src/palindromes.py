# Write your solution here
# Note, that at this time the main program should not be written inside
def palindromes(teks):
    list = ""
    for i in reversed(teks):
        list += i
    
    if list == teks:
        return True
    else:
        return False
# if __name__ == "__main__":
# block!
while True:
    string = str(input("Please type in a palindrome: "))
    if palindromes(string):
        print(f"{string} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")
        