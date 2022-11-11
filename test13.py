import turtle
t = turtle.Turtle()
t.shape("turtle")

def squre(a):
    for i in range(4):
        t.forward(a)
        t.left(90)


squre(200)
turtle.done()