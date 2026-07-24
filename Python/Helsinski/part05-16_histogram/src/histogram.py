# Write your solution here
def histogram(teks: str):
    dict = {}
    for i in teks:
        if i not in dict:
            dict[i] = 0
        dict[i] += 1

    for character, value in dict.items():
        print(f"{character} {value * "*"}")
if __name__ == "__main__":
    histogram("abba")