# Odd/Even:
# Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.
def odd_even():
    for i in range(1, 2001):
        if i % 2 == 0:
            num_type = "even"
            print "Number is {}. This is an {} number.".format(i, num_type)
        else:
            num_type = "odd"
            print "Number is {}. This is an {} number.".format(i, num_type)
odd_even()

# Multiply:
# Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
a = [2, 4, 10, 16]

def multiply(lst, num):
    for i in range(0, len(lst)):
        lst[i] = lst[i] * num
    return lst

new_list = multiply(a,5)
print "New list:", new_list

# Hacker Challenge:
# Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list. Each internal list should contain the 1's times the number in the original list.
def layered_multiples(lst):
    new_list = []
    for i in lst:
        val_lst = []
        for x in range(0,i):
            val_lst.append(1)
        new_list.append(val_lst)
    return new_list

x = layered_multiples(multiply([2,4,5],3))
print x