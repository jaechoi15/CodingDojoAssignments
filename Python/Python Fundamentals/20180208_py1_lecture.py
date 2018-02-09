# my_list = [41,23]
# my_second_list = [
#     42,24
# ]

# try:
#     print my_list[1] + my_second_list[2]
# except IndexError:
#     print my_list[0] + my_second_list[1]

# myList = [25]
# def add5(myNum):
#     myNum += 5
#     print myNum

# add5(myList)
# print myList

# i,j = (1,2), [3,4]
# i[1] = 42
# j[0] = 42
# print i[1] + j[1]

# our_list = ['Marti', 'Michael']

# our_value= enumerate(our_list)
# for val in our_value:
#     print val
# for idx, value in enumerate(our_list):
#    

# name = {
#     "sw": "sara wong",
#     "mp":"martin puryear"
# }

# for key, value in name.iteritems():
#     print key, value

# import turtle
# # the distance we want the pointer to travel each time
# shannon = turtle.Turtle()
# nate = turtle.Turtle()

# DIST = 100
# circle_size = 15
# for x in range(8): # make an octogon
#     print shannon.position()
#     shannon.shape('turtle')
#     shannon.color('#002244')
#     shannon.forward(DIST)
#     shannon.left(45)
# for y in range(4):  # make some concentric circles going out
#     nate.setx(50)
#     nate.sety(50)
#     print nate.position()
#     nate.shape('classic')
#     nate.speed(1)
#     nate.fill(True)
#     nate.color('#69be28')
#     nate.circle(circle_size)
#     nate.fill(False)
#     circle_size += 15
# nate.dot(20, "#002244") # end with a dot

# import turtle
# loadWindow = turtle.Screen()
# turtle.speed(30)
# def tree(branchLen,t):
#     t.color("green")
#     if branchLen > 5: #if branch length greater than 5, branch again
#         if branchLen <20:
#             t.color("red") #if branch length getting small, change to color red
#         t.forward(branchLen)
#         t.color("green")
#         t.right(20)
#         tree(branchLen-10,t)
#         t.left(40)
#         tree(branchLen-10,t)
#         t.right(20)
#         t.penup()
#         t.backward(branchLen)
#         t.pendown()

# def main():
#     t = turtle.Turtle()
#     myWin = turtle.Screen()
#     t.left(90)
#     t.up()
#     t.backward(200)
#     t.down()
#     tree(75,t)
#     myWin.exitonclick()

# main()

import turtle

me = turtle.Turtle()

me.speed(10)

def long_wing():
    for i in range(50):
        me.forward(100)
        me.right(30)
        me.forward(20)
        me.left(60)
        me.forward(50)
        me.right(30)

        me.penup()
        me.setposition(0,0)
        me.pendown()
        me.right(2)

def short_wing():
    for i in range(50):
        me.forward(50)
        me.right(30)
        me.forward(20)
        me.left(60)
        me.forward(50)
        me.right(30)

        me.penup()
        me.setposition(0,0)
        me.pendown()
        me.right(2)

me.pencolor("red")
long_wing()
me.pencolor("blue")
short_wing()
me.pencolor("red")
long_wing()
me.pencolor("blue")
short_wing()

turtle.done()
# # Draw a square
# def square():
#     me.pencolor("red")
#     for i in range(4):
#         me.forward(50)
#         me.right(90)

# # # Draw a star
# # for i in range(50):
# #     me.forward(50)
# #     me.right(144)
# def star():
#     me.pencolor("blue")
#     for i in range(21):
#         me.forward(i*10)
#         me.right(144)

# square()
# star()
# square()
