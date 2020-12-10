num_employees = int(input("Please enter number of employees: "))
employee_info = {}
employee_data = ['Age', 'City', 'Department']
for i in range(0,num_employees):
    name = input("Enter Employee Name: ")
    employee_info[name] = {}
    for entry in employee_data:
        employee_info[name][entry] = input(entry+": ")
print(employee_info)