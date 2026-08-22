# Write your solution here
import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
age = datetime.date(year, month, day)
milenium = datetime.date(1999, 12, 31)


if age < milenium:
    difference = milenium - age
    print(f"You were {difference.days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")