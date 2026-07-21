# Write your solution here
string = str(input("Word: "))
star = "*"
num = " "
space = 28 - len(string)
left = space // 2
right = space - left
print(star * 30)
print(star + (num * left) + string + (num *right) + star)
print(star * 30)