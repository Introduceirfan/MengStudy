# Write your solution here
wage = float(input("Hourly wage: "))
work = int(input("Hours worked: "))
week = input("Day of the week: ")
if week != "Sunday":
    print(f"Daily wages: {wage*work} euros")
else:
    print(f"Daily wages: {(wage*work) * 2} euros")
