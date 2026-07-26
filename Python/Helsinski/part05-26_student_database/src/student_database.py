# Write your solution here
def add_student(database, name):
    database[name] = []
    
def add_course(database, name, course):
     if name in database:
          if course[1] == 0:
               return
          for i in range(len(database[name])):
               if course[0] == database[name][i][0]:
                    if course[1] > database[name][i][1]:
                        database[name][i] = course
                    return
          database[name].append(course)

def print_student(database, name):
        if name in database:
            print(f"{name}:")
            if len(database[name]) == 0:
                print(" no completed courses")
            else:
                print(f" {len(database[name])} completed courses:")
                total_grade = 0
                for c in database[name]:
                    print(f"  {c[0]} {c[1]}")
                    total_grade += c[1]
                print(f" average grade {total_grade/len(database[name])}")
        else:
             print(f"{name}: no such person in the database")

def summary(database):
    print(f"students {len(database)}")

    most_course = ""
    most_course_count = 0

    best_average = ""
    best_average_count = 0

    for name in database:
        temp = len(database[name])
        if temp > most_course_count:
            most_course_count = temp
            most_course = name
        if temp > 0:
            total_grade = 0
            for course in database[name]:
                total_grade += course[1]
            average = total_grade/temp

            if average > best_average_count:
                best_average_count = average
                best_average = name

    print(f"most courses completed {most_course_count} {most_course}")
    print(f"best average grade {best_average_count} {best_average}")
              

if __name__ == "__main__":     
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)