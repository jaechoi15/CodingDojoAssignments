# Part 1

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def studentNames(students):
    for val in students:
        print val['first_name'], val['last_name']

studentNames(students)

# Part II

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def studentsAndInstructors(users):
    for job in users:
        count = 0
        print job
        for val in users[job]:
            count += 1
            length = len(val['first_name']) + len(val['last_name'])
            print str(count) + " " + val['first_name'].upper() + " " + val['last_name'].upper() + " - " + str(length)

studentsAndInstructors(users)