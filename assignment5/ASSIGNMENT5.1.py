
student_marks = {'Alice': 85,'Bob': 92,'Charlie': 78,'Diana': 88,'Ethan': 90}

name = input("Enter the student's name: ")

if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")