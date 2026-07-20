# Write your solution here
list = []
i = 1

while True:
    print(f"The list is now {list}")
    formu = input("a(d)d, (r)emove or e(x)it: ")
    
    if formu == "d":
        list.append(i)
        i += 1
        
    if formu == "r":
        if len(list) > 0:
            list.pop()
            i -= 1
            
    if formu == "x":
        break

print("Bye!")