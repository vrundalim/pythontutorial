data = [
      {'name': 'Alice23', 'age': 16, 'grade': 88, 'city': 'New York', 'gender': 'Female', 'subject': 'Math', 'attendance': 95, 'height': 162.5, 'favorite_color': 'Blue', 'hobby': 'Reading'},
    {'name': 'Bob47', 'age': 17, 'grade': 92, 'city': 'Miami', 'gender': 'Male', 'subject': 'Science', 'attendance': 88, 'height': 175.2, 'favorite_color': 'Red', 'hobby': 'Gaming'},
    {'name': 'Charlie5', 'age': 15, 'grade': 78, 'city': 'Chicago', 'gender': 'Male', 'subject': 'English', 'attendance': 80, 'height': 168.3, 'favorite_color': 'Green', 'hobby': 'Swimming'},
    {'name': 'David12', 'age': 16, 'grade': 85, 'city': 'Houston', 'gender': 'Male', 'subject': 'History', 'attendance': 90, 'height': 172.4, 'favorite_color': 'Yellow', 'hobby': 'Cycling'},
    {'name': 'Eva34', 'age': 17, 'grade': 95, 'city': 'Seattle', 'gender': 'Female', 'subject': 'Art', 'attendance': 97, 'height': 158.7, 'favorite_color': 'Purple', 'hobby': 'Drawing'},
    {'name': 'Frank8', 'age': 18, 'grade': 82, 'city': 'Boston', 'gender': 'Male', 'subject': 'Music', 'attendance': 85, 'height': 180.5, 'favorite_color': 'Orange', 'hobby': 'Dancing'},
    {'name': 'Grace16', 'age': 15, 'grade': 89, 'city': 'San Francisco', 'gender': 'Female', 'subject': 'Math', 'attendance': 92, 'height': 165.8, 'favorite_color': 'Pink', 'hobby': 'Singing'},
    {'name': 'Hannah9', 'age': 16, 'grade': 91, 'city': 'Denver', 'gender': 'Female', 'subject': 'Science', 'attendance': 94, 'height': 160.2, 'favorite_color': 'Blue', 'hobby': 'Hiking'},
    
]
#filter func
#age is grater than 16
# print(list(filter(lambda h : h['age'] > 16,data)))

# #favorite color is blue
# print(list(filter(lambda j : j['favorite_color'] == 'Blue',data)))

# #grade is higher than 90
# print(list(filter(lambda k : k['grade'] > 90,data)))

# #female students
# print(list(filter(lambda b : b['gender'] == 'Female',data)))

# #attendence is below 90
# print(list(filter(lambda l : l ['attendance'] < 90,data)))
                    
#map func
#name of students
# print(list(map(lambda b : b['name'],data)))
# #Create a list of all student ages.
# print(list(map(lambda j : j['age'],data)))
# # Create a list of all grades of the students.
# print(list(map(lambda b : b['grade'],data)))
# # Create a list of name and grade pairs for all students.
# print(list(map(lambda v: (v['name'] ,v['grade']),data)))
# # Create a list of cities where the students live.
# print(list(map(lambda h : h['city'],data)))

# combing
# get the names of students older than 16.
# b= list(map(lambda j : (j['name'],j['age']),filter(lambda j: j['age'] > 16,data)))
# print(b)
# # Get the grades of female students.
# v  = list(map(lambda j : (j['name'],j['gender'],j['grade']),filter(lambda j : j['gender'] == 'Female',data)))
# print(v)
# # Get the names of students whose grade is above 90.
# l = list(map(lambda j :(j['name'],j['grade']),filter(lambda j : j['grade'] > 90,data)))
# print(l)
# # Get the favorite colors of students whose hobby is 'Gaming' or 'Swimming'.
# k = list(map(lambda j : (j['name'],j['favorite_color'],j['hobby']),filter(lambda j: j['hobby'] == 'Gaming' or j['hobby'] == 'Swimming',data) ))
# print(k)
# # Get the height of students with attendance above 90.
# d = list(map(lambda j : (j['name'],j['height'],j['attendance']),filter(lambda j: j['attendance'] > 90,data)))
# print(d)



employees_20 = [
    {'name': 'Alex01', 'age': 28, 'salary': 55000, 'department': 'HR', 'gender': 'Male', 'experience': 4, 'city': 'New York', 'performance': 8.2, 'bonus': 5000, 'status': 'Active'},
    {'name': 'Brenda02', 'age': 32, 'salary': 72000, 'department': 'Finance', 'gender': 'Female', 'experience': 7, 'city': 'Chicago', 'performance': 9.1, 'bonus': 8000, 'status': 'Active'},
    {'name': 'Carlos03', 'age': 26, 'salary': 48000, 'department': 'IT', 'gender': 'Male', 'experience': 3, 'city': 'Austin', 'performance': 7.5, 'bonus': 4000, 'status': 'Active'},
    {'name': 'Diana04', 'age': 29, 'salary': 65000, 'department': 'Marketing', 'gender': 'Female', 'experience': 5, 'city': 'Boston', 'performance': 8.8, 'bonus': 6000, 'status': 'Active'},
    {'name': 'Ethan05', 'age': 35, 'salary': 85000, 'department': 'IT', 'gender': 'Male', 'experience': 10, 'city': 'Seattle', 'performance': 9.4, 'bonus': 10000, 'status': 'Active'},
    {'name': 'Farah06', 'age': 27, 'salary': 52000, 'department': 'HR', 'gender': 'Female', 'experience': 3, 'city': 'Denver', 'performance': 7.9, 'bonus': 4500, 'status': 'Active'},
    {'name': 'George07', 'age': 31, 'salary': 70000, 'department': 'Finance', 'gender': 'Male', 'experience': 6, 'city': 'San Diego', 'performance': 8.6, 'bonus': 7500, 'status': 'Active'},
    {'name': 'Hina08', 'age': 25, 'salary': 46000, 'department': 'Marketing', 'gender': 'Female', 'experience': 2, 'city': 'Los Angeles', 'performance': 7.2, 'bonus': 3000, 'status': 'Active'},
    {'name': 'Ivan09', 'age': 34, 'salary': 78000, 'department': 'IT', 'gender': 'Male', 'experience': 8, 'city': 'New York', 'performance': 9.0, 'bonus': 8500, 'status': 'Active'},
    {'name': 'Julia10', 'age': 30, 'salary': 68000, 'department': 'HR', 'gender': 'Female', 'experience': 5, 'city': 'Chicago', 'performance': 8.4, 'bonus': 6200, 'status': 'Active'},
    {'name': 'Kevin11', 'age': 29, 'salary': 60000, 'department': 'Sales', 'gender': 'Male', 'experience': 4, 'city': 'Houston', 'performance': 8.0, 'bonus': 5500, 'status': 'Active'},
    {'name': 'Lara12', 'age': 33, 'salary': 74000, 'department': 'Finance', 'gender': 'Female', 'experience': 7, 'city': 'Phoenix', 'performance': 8.9, 'bonus': 8200, 'status': 'Active'},
    {'name': 'Mike13', 'age': 27, 'salary': 51000, 'department': 'Sales', 'gender': 'Male', 'experience': 3, 'city': 'Dallas', 'performance': 7.6, 'bonus': 4200, 'status': 'Active'},
    {'name': 'Nina14', 'age': 36, 'salary': 90000, 'department': 'IT', 'gender': 'Female', 'experience': 11, 'city': 'San Jose', 'performance': 9.6, 'bonus': 12000, 'status': 'Active'},
    {'name': 'Omar15', 'age': 28, 'salary': 56000, 'department': 'Marketing', 'gender': 'Male', 'experience': 4, 'city': 'Orlando', 'performance': 8.1, 'bonus': 5000, 'status': 'Active'},
    {'name': 'Priya16', 'age': 31, 'salary': 71000, 'department': 'Finance', 'gender': 'Female', 'experience': 6, 'city': 'San Francisco', 'performance': 8.7, 'bonus': 7800, 'status': 'Active'},
    {'name': 'Rahul17', 'age': 26, 'salary': 49000, 'department': 'IT', 'gender': 'Male', 'experience': 2, 'city': 'Austin', 'performance': 7.4, 'bonus': 3500, 'status': 'Active'},
    {'name': 'Sara18', 'age': 34, 'salary': 82000, 'department': 'HR', 'gender': 'Female', 'experience': 9, 'city': 'New York', 'performance': 9.2, 'bonus': 9500, 'status': 'Active'},
    {'name': 'Tom19', 'age': 38, 'salary': 88000, 'department': 'Sales', 'gender': 'Male', 'experience': 12, 'city': 'Chicago', 'performance': 8.9, 'bonus': 9000, 'status': 'Active'},
    {'name': 'Uma20', 'age': 24, 'salary': 45000, 'department': 'Marketing', 'gender': 'Female', 'experience': 1, 'city': 'San Diego', 'performance': 7.1, 'bonus': 2500, 'status': 'Active'}
]

# Filter employees whose salary is greater than 70,000.
# print(list(filter(lambda j : j['salary'] > 70000,employees_20)))

# Filter employees working in the IT department.
# print(list(filter(lambda j : j['department'] == 'IT',employees_20)))

# Filter employees who have more than 5 years of experience.
# print(list(filter(lambda j : j['experience'] > 5,employees_20)))

# Filter employees who live in New York.
# print(list(filter(lambda j : j['city'] == 'New York',employees_20)))

# Filter female employees whose performance score is above 9.0.
# print(list(filter(lambda j : j['performance'] > 9,employees_20)))

# Filter employees whose bonus is less than 5,000.
# print(list(filter(lambda j : j['bonus'] < 5000,employees_20)))

# # Filter employees older than 30 and working in Finance.
# print(list(filter(lambda j: j['age'] > 30 and j['department'] == 'Finance',employees_20)))

#map function
#Create a list of all employee names.
# print(list(map(lambda j : j['name'],employees_20)))

# Create a list of salaries increased by 10%.
# print(list(map(lambda j: j['salary']+j['salary']*10/100,employees_20)))

# Create a list of tuples (name, department) for all employees.
# print(list(map(lambda j: (j['name'],j['department']),employees_20)))

# Create a list showing each employee’s performance grade
# (Excellent ≥ 9, Good ≥ 8, Average < 8).

# def myfunction(employees):
#   if employees['performance'] >= 9:
#         return "Excelllent"
#   elif employees['performance'] >= 8:
#          return "Good"
#   else:
#         return "Average"
# a = list(map(myfunction , employees_20))
# print(a)

# Convert all employee salaries from yearly to monthly salary.
# print(list(map(lambda j : j['salary'] * 12,employees_20)))

# 🔹 LIST COMPREHENSION QUESTIONS

# Create a list of names of employees who work in Marketing.
# a = []
# def mt(emp):
#     if emp['department'] == "Marketing":
#         return 'Marketing'
# a = list(filter(mt , employees_20))
# print(a)

# a = [emp['name'] for emp in employees_20 if emp['department'] == "Marketing" ]
# print(a)

# Create a list of salaries of employees who have more than 5 years of experience.
# a = [emp['salary'] for emp in employees_20 if emp['experience'] > 5]
# print(a)

# Create a list of (name, bonus) for employees whose bonus is greater than 7,000.
# a = [(emp['name'],emp['bonus']) for emp in employees_20 if emp['bonus'] > 7000]
# print(a)

# Create a list of employee names who live in Chicago or New York.
# a = [(emp['name'],emp['city']) for emp in employees_20 if emp['city'] == 'Chicago' or emp['city'] == 'New York']
# print(a)

# Create a list of employees whose performance score is above the average performance.

# 🔹 MIXED PRACTICE (Filter + Map vs List Comprehension)

# Using filter() and map(), get the names of employees whose salary is below 60,000.
a = list(map(lambda j : (j['name'],j['salary']),filter(lambda j : j['salary'] < 60000,employees_20)))
print(a)
# Using list comprehension, get the names of employees whose salary is below 60,000.
a = [(emp['name'],emp['salary']) for emp in employees_20 if emp['salary'] < 60000]
print(a)
# Using list comprehension, create a list of departments without duplicates.

a = {emp['department'] for emp in employees_20 }
print(a)





 



