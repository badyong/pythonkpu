import turtle
t = turtle.Turtle()
t.speed()
t.width(3)
length = 10
while length < 500:
    t.forward(length)
    t.right(89)
    length +=5
turtle.done()