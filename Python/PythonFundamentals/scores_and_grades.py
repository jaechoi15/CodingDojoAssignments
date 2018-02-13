# Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score.
# Grade Table:
# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A
import random

def scores_grades():
    print "Scores and Grades"
    for i in range(0,10):
        random_num = random.randint(60,100)
        if random_num >= 60 and random_num <= 69:
            grade = "D"
            print "Score: {}; Your grade is {}".format(random_num, grade)
        elif random_num >= 70 and random_num <= 79:
            grade = "C"
            print "Score: {}; Your grade is {}".format(random_num, grade)
        elif random_num >= 80 and random_num <= 89:
            grade = "B"
            print "Score: {}; Your grade is {}".format(random_num, grade)
        else:
            grade = "A"
            print "Score: {}; Your grade is {}".format(random_num, grade)
    print "End of the program. Bye!"

scores_grades()