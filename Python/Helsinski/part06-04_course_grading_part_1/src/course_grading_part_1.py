# write your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

students = {}
with open(student_info) as student_file:
    for line in student_file:
        student_parts = line.split(';')
        if  student_parts[0] == "id":
            continue
        full_name = student_parts[1] + " " + student_parts[2].strip()
        students[student_parts[0]] = full_name

exercise = {}
with open(exercise_data) as exercise_file:
    for line in exercise_file:
        exercise_parts = line.split(';')
        if exercise_parts[0] == "id":
            continue
        grade = []
        for grades in exercise_parts[1:]:
            grade.append(int(grades))
        exercise[exercise_parts[0]] = sum(grade)

for id, name in students.items():
    if id in exercise:
        print(f"{name} {exercise[id]}")
