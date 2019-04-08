from turtle import *
def draw_square(length, color):
        shape("turtle")
        pencolor(color)
        for i in range(4):
                left(90)
                forward(length)
        return length, color

speed(0)

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()