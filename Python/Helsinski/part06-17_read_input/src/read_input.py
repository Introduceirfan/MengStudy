# Write your solution here
def read_input(str_input, x, y):
    while True:
        try:
            inputs = int(input(str_input))
            if inputs >= x and inputs <= y:
                return inputs
        except:
            pass
        print(f"You must type in an integer between {x} and {y}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)
