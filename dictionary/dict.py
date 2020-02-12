student = {'name': "Ram Krishna", 'age': 20, 'level': "bachelor"}
print(student)
print(student['name'])
print(student['level'])
student['age'] = 4
student['address'] = 'Sankhu'
print(student)
for x in student.values():
    print(x)
