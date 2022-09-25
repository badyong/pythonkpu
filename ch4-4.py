import turtle
t = turtle.Turtle()
t.shape("turtle")

t.penup()
t.goto(100,100)
t.write("두 수 모두 양수.")
t.goto(-100,100)
t.write("첫번째 수만 음수")
t.goto(-100,-100)
t.write("두 수 모두 음수")
t.goto(100,-100)
t.write("두번째 수만 음수")
t.goto(0,0)
t.pendown()

n1 = turtle.textinput("","첫번째 좌표를 입력하세요")
n2 = turtle.textinput("","두번쨰 좌표를 입력하세요")
x = int(n1)
y = int(n2) 
if x > 0 and y > 0:
    t.goto(100,100)
if x < 0 and y > 0:
    t.goto(-100,100)
if x < 0 and y < 0:
    t.goto(-100,-100)
if x > 0 and y < 0:
    t.goto(100,-100)

trutle.done()
