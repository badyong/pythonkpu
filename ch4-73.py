import turtle
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.shapesize(3,3)
while True:
    num = int(input("1~9까지의 숫자를 입력하세요"))
    t.shapesize(num,num)