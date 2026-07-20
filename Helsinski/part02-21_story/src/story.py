# Write your solution here
con = ""
last = "whep"
while True:
    inp = input("Please type in a word: ")
    if inp == last:
        break
    last = inp
    if inp == "end":
        break
    con += inp + " "
print(con)