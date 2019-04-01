from turtle import *
speed(0)
shape("turtle")
color = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in color:
    fillcolor(i)
    pencolor(i)
    begin_fill()
    for i in range(2):
        forward(50)        
        left(90)
        forward(100)
        left(90)
    end_fill()
    forward(50)
mainloop()
