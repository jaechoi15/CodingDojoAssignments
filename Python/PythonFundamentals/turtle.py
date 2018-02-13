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