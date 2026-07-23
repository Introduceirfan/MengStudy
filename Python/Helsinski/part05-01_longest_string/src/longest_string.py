# Write your solution here
def longest(text):
    best = text[0]
    for i in text:
        if len(i) >= len(best):
            best = i
    return best

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))