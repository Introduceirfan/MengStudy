# Write your solution here
def add_student(database, name):
    database[name] = []

def add_course(database, name, course):
     if name in database:
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
if __name__ == "__main__":     
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    print_student(students, "Peter")