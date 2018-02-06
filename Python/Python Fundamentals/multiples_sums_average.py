# Multiples
# Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.
for x in range(0, 1000):
    if x % 2 != 0:
        print "Part I:", x

# Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.
for x in range (0, 1000000):
    if x % 5 == 0:
        print "Part II:", x

# Sum List
# Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3]
total = sum(a)
print "Sum of List:", total

# Average List
# Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3]
avg = sum(a)/len(a)
print "Average:", avg