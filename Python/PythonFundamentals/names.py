# Part I
# Given the following list. Create a function.
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# def student_names(lst):
#     for x in students:
#         print x["first_name"], x["last_name"]

# student_names(students)

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

def students_instructors(mydictionary):
    for key in users:
        print key
        position = 0

        for user in users[key]:
            position += 1
            first_name = user["first_name"].upper()
            last_name = user["last_name"].upper()
            name_length = len(first_name) + len(last_name)
            print position, first_name, last_name, "-", name_length

students_instructors(users)