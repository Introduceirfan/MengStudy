# Write your solution here
sentence = str(input("Please type in a sentence: "))
i = 0
while i < len(sentence):
    if i == 0:
        print(sentence[0])
    if sentence[i] == " ":
        print(sentence[i + 1])
    i += 1
