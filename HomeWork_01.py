import turtle
# ทดลองuploadเข้าGitHub
tao = turtle.Pen()
tao.shape('turtle')
tao.color("black", "red")
tao.begin_fill()
tao.home()
tao.setheading(90)
for i in range (5):
    tao.forward(50)
    tao.right(90)
    for j in range (1):
        tao.forward(50)
        tao.left(90)
tao.setheading(270)
for i in range (5):
    tao.forward(50)
    tao.right(90)
    for j in range (1):
        tao.forward(50)
        tao.left(90)
tao.end_fill()
tao.color("black", "blue")
tao.begin_fill()
tao.goto(0,-50)
tao.setheading(90)
for i in range (5):
    tao.forward(50)
    tao.right(90)
    for j in range (1):
        tao.forward(50)
        tao.left(90)
tao.setheading(270)
for i in range (5):
    tao.forward(50)
    tao.right(90)
    for j in range (1):
        tao.forward(50)
        tao.left(90)


tao.end_fill()
turtle.done()

