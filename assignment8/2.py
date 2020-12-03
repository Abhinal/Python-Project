num_students = int(input("Please enter number of students: "))
student_info = {}
student_data = ['Student Name', 'Class', 'Subjects']
for i in range(0,num_students):
    student_info[i+1] = {}
    for entry in student_data:
        student_info[i+1][entry] = input(entry+": ")
print(student_info)

result = {}
for key,value in student_info.items():
    if value not in result.values():
        result[key] = value
print(result)
