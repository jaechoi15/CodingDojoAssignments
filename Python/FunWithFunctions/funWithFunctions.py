# Odd/Even:
# Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.

def odd_even():
    for i in range (1, 21, 1):
        if i % 2 == 1:
            print "Number is " + str(i) + ". This is an odd number."
        else:
            print "Number is " + str(i) + ". This is an even number."

odd_even()

# Multiply:
# Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.

a = [2, 4, 10, 16]

def multiply(a,num):
    for i in range (0,len(a)):
        a[i] *= num
    return a

print multiply(a,5)

# Hacker Challenge:
# Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list. Each internal list should contain the 1's times the number in the original list.

def layered_multiples(arr):
    new_array = []
    for y in arr:
        new_array2 = []
        count = 0
        while count < y:
            new_array2.append(1)
            count += 1
        new_array.append(new_array2)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x
