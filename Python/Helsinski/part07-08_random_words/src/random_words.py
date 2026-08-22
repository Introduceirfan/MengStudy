# Write your solution here
from random import sample
def words(n, beginnning):
    rand_word = []
    with open("words.txt") as new_file:
        for line in new_file:
            word = line.strip()
            if word.startswith(beginnning):
                rand_word.append(word)

    if len(rand_word) < n:
        raise ValueError('bad')
    
    return sample(rand_word, n)

if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)