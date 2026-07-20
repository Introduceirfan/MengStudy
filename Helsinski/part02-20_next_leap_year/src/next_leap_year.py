# Write your solution here
year = int(input("Year: "))
fel = year
while True:
    fel += 1
    if fel % 100 == 0 and fel % 400 == 0:
        break
    if fel % 4 == 0:
        if fel % 100 == 0:
            continue
        break
print(f"The next leap year after {year} is {fel}")