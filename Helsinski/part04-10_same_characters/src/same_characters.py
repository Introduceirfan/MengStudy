def same_chars(str, a, b):
    if a >= len(str) or b >= len(str):
        return False
    return str[a] == str[b]
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", -1, 1))