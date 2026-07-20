# Write your solution here
grade = int(input("How many points [0-100] : "))
if grade <= 100 and grade >= 90:
    print("Grade: 5")
elif grade <= 89 and grade >= 80:
    print("Grade: 4")
elif grade <= 79 and grade >= 70:
    print("Grade: 3")
elif grade <= 69 and grade >= 60:
    print("Grade: 2")
elif grade <= 59 and grade >= 50:
    print("Grade: 1")
elif grade <= 49 and grade >= 0:
    print("Grade: fail")
else:
    print("Grade: impossible!")