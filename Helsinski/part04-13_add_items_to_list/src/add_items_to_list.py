# Write your solution here
items = int(input("How many items: "))
list = []
i = 1
while i <= items:
    temp = int(input(f"Item{i}: "))
    list.append(temp)
    i += 1
print(list)