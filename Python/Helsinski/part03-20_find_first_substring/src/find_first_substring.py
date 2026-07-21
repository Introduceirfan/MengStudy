# Write your solution here
word = str(input("Please type in a word: "))
chara = str(input("Please type in a character: "))
rem = word.find(chara) 
if rem != -1 and rem + 2 < len(word):
    print(word[rem:rem+3])
