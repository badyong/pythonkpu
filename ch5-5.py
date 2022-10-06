import turtle
t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("","몇각형을 원하시나요?:")
s2 = turtle.textinput("","한 변의 길이는 얼마를 원하시나요?:")
n = int(s)
n2 = int(s2)
for i in range(n):
    t.forward(n2)
    t.left(360/n)
turtle.done()