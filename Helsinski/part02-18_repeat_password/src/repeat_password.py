# Write your solution here
un = input("Password: ")
while True:
    rep = input("Repeat password: ")
    if rep == un :
        break
    else:
        print("They do not match!")
print("User account created!")