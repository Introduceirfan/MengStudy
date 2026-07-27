# write your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")

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

exam_points = {}
with open(exam_data) as exam_file:
    for line in exam_file:
        exam_parts = line.split(';')
        if exam_parts[0] == "id":
            continue
        sum_exam = []
        for egrade in exam_parts[1:]:
            sum_exam.append(int(egrade))
        exam_points[exam_parts[0]] = sum(sum_exam)

print(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}")
for id, name in students.items():
    total_exercise = exercise[id]
    exercise_points = total_exercise // 4

    exam_convert = exam_points[id]
    total_points = exercise_points + exam_convert

    if total_points >= 28:
        student_grade = 5
    elif total_points >= 24:
        student_grade = 4
    elif total_points >= 21:
        student_grade = 3
    elif total_points >= 18:
        student_grade = 2
    elif total_points >= 15:
        student_grade = 1
    else:
        student_grade = 0

    print(f"{name:30}{exercise[id]:<10}{exercise_points:<10}{exam_convert:<10}{total_points:<10}{student_grade:<10}")
    