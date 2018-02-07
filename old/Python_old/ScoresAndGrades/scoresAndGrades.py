# Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:
# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A

from random import randint

def scores_grades(num):
    print "Scores and Grades"
    for i in range (0,num):
        score = randint(60,100)
        if score < 70:
            print "Score:", score," Your grade is D"
        elif score > 69 and score < 80:
            print "Score:", score," Your grade is C"
        elif score > 79 and score < 90:
            print "Score:", score," Your grade is B"
        else:
            print "Score:", score, " Your grade is A"
    print "End of the program. Bye!"

scores_grades(30)