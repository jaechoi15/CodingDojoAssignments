# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.
# Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.

# input
lst = ['magical unicorns',19,'hello',98.98,'world']
# lst = [2,3,1,7,4,12]
# lst = ['magical','unicorns']

sum = 0
new_string = ""
str_list = False
num_list = False

for i in range(0, len(lst)):
    if type(lst[i]) == str:
        new_string += " " + lst[i]
        str_list = True

    elif type(lst[i]) == int or float:
        sum += lst[i]
        num_list = True

# If the list contains both string and integer/float items
if str_list and num_list:
    print "The list you entered is of mixed type"
    print "String:", new_string
    print "Sum:", sum

# If the list contains only string items
elif str_list:
    print "The list you entered is of string type"
    print "String:", new_string

# If the list contains only integer/float items
else:
    print "The list you entered is of integer type"
    print "Sum:", sum