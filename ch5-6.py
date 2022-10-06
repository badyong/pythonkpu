import turtle
import random
t = turtle.Turtle()
t.shape("turtle")
li = [90,180,270,360]

for i in range(30):
    length = random.randint(1,100)
    t.forward(length)
    angle = random.choice(li)
    t.right(angle)
turtle.done()