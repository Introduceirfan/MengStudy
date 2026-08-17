# Write your solution here
import string 

def separate_characters(mystr):
    letters = ""
    punctuation = ""
    others = ""
    for i in mystr:
        if i in string.ascii_letters:
            letters += i
        elif i in string.punctuation:
            punctuation += i
        else:
            others += i

    return letters, punctuation, others
 
if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])