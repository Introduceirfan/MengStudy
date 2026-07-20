# Write your solution here
def first_word(sentenced):
    return sentenced[0:sentenced.find(" ")]

def second_word(sentenced):
    space = sentenced.find(" ")
    index2 = space + 1
    space2 = sentenced.find(" ", index2)
    if space2 == -1:  
        return sentenced[index2:]   
    return sentenced[index2:space2]
def last_word(sentenced):
    return sentenced[sentenced.rfind(" ") + 1:]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))