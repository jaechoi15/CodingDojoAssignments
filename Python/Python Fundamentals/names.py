# Part I
# Given the following list. Create a function.
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def student_names(lst):
    for i in range(0,len(lst)):
        print lst[i]["first_name"], lst[i]["last_name"]

student_names(students)

# for student in students:
#     print student["first_name"], student["last_name"]

# Part II
# Given the following dictionary. Create a function.
users = {
 'Students': [
     {'first_name' : 'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def students_instructors(users):
    for key in users:
        print key
        position = 0

        for person in users[key]:
            position += 1
            first_name = person["first_name"].upper()
            last_name = person["last_name"].upper()
            name_length = len(person["first_name"]) + len(person["last_name"])
            print position, "-", first_name, last_name, "-", name_length 

students_instructors(users)