# Write your solution here
limit = int(input("Limit: "))
il = 0
lem = 1
whe = "1"
while il < limit:
    il += lem
    if lem != 1:
        whe += f" + {str(lem)}"
    lem += 1
print(f"The consecutive sum: {whe} = {il}")