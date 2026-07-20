# Write your solution here
while True:
    inp = str(input("Editor: "))
    ren= inp.lower()
    if ren == "visual studio code":
        print("an excellent choice!")
        break
    if ren == "word" or ren == "notepad":
        print("awful")
    else:
        print("not good")