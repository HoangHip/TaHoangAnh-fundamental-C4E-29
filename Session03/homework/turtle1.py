from turtle import *
speed(0)
shape("turtle")
color = ['red', 'blue', 'brown', 'yellow', 'grey']
x = 180-(360*5)/14
pencolor(color[0])
for i in range (3):
    left(120)
    forward(100)
pencolor(color[1])
for i in range (4):
    left(90)
    forward(100)
pencolor(color[2])
for i in range(5):
    left(72)
    forward(100)
pencolor(color[3])
for i in range(6):
    left(60)
    forward(100)
pencolor(color[4])
for i in range(7):
    left(x)
    forward(100)


mainloop()  