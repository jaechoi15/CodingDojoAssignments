# Write a program that prints a 'checkerboard' pattern to the console.

def checkerboard():
    for i in range (1, 9, 1):
        if i % 2 == 1:
            print '* * * * '
        else:
            print ' * * * *'

checkerboard()