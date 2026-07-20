# Write your solution here
word = str(input("Please type in a word: "))
chara = str(input("Please type in a character: "))

while True:
    rem = word.find (chara)
    if rem == -1 or rem + 2 >= len(word) :
        break
    if chara not in word:
        break
    if chara in word:
        print(word[rem:rem+3])
        word = word[rem+1:]
