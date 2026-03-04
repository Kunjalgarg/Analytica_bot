from turtle import *

bgcolor("black")
pencolor("#9f0000")
pensize(1)

penup()
goto(-45,-180)
pendown()
begin_fill()
for i in range(2):
    fillcolor("#ef0000")
    left(90)
    fd(400)
    left(90)
    fd(70)
end_fill()

penup()
goto(100,-180)
pendown()
begin_fill()
for i in range(2):
    fillcolor("#ef0000")
    left(90)
    fd(400)
    left(90)
    fd(70)
end_fill()

penup()
goto(100,-180)
pendown()
begin_fill()
for i in range(2):
    fillcolor("red")
    left(110)
    fd(425)
    left(70)
    fd(70)
end_fill()
hideturtle()
done()
