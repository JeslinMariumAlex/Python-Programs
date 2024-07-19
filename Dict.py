n = int(input("Enter the number of Employees:"))
emp_dict = {}
for i in range(0, n):
    emp_name = input("Enter the name of employee:")
    salary = int(input("Enter the salary:"))
    emp_dict[emp_name] = salary
print("Employee details:")
print(emp_dict)
