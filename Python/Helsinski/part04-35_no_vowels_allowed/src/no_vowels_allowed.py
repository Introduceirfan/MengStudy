# Write your solution here
def no_vowels(teks : str):
    vowels = "aiueo"
    ma_string = ""
    for i in teks:
        if i not in vowels:
            ma_string += i
    return ma_string

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))