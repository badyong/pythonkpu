import turtle
t = turtle.Turtle()
t.shape("turtle")

t.penup()
t.goto(100,100)
t.write("첫번 째 수가 더 큽니다.")
t.goto(-100,100)
t.write("두번 째 수가 더 큽니다")
t.goto(0,200)
t.write("두 수가 동일합니다")
t.goto(0,100)
t.pendown()

n1 = turtle.textinput("","첫번째 좌표를 입력하세요")
n2 = turtle.textinput("","두번쨰 좌표를 입력하세요")
x = int(n1)
y = int(n2) 
if x > y :
    t.goto(100,100)
elif x < y:
    t.goto(-100,100)
else:
    t.goto(0,200)

trutle.done()