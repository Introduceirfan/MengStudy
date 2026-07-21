# Write your solution here
student = int(input("How many students on the course? "))
desire = int(input("Desired group size? "))
print(f"Number of groups formed: {(student + desire - 1)//desire}")