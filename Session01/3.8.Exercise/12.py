from turtle import *
shape("turtle")
pencolor("blue")
color("blue")

for i in range(12):
    penup()
    forward(150)
    pendown()
    forward(20)
    penup()
    forward(20)
    pendown()
    stamp()
    left(180)
    penup()
    forward(190)
    pendown()
    left(30)
mainloop()