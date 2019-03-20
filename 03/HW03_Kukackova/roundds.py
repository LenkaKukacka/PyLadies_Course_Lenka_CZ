# triangle
from turtle import pen, speed, setposition, screensize, setup, goto, forward, left, right, down, up, backward, penup, pendown, exitonclick, shape
screensize ()
setup (width = 1.0, height = 1.0)

shape ("turtle")
pen (fillcolor = "red", pensize = 2)

#presun + ctvrtcovy ornament
for action in range (1):
    penup ()
    setposition (-500,0) #goto
    pendown ()

s = 10
for iteration in range (20):
    left (90)
    forward (s)
    s = (s + (10/2))

#presun + ornament kulaty
for action in range (1):
    penup ()
    setposition (-300,0)
    pendown ()

s = 5
for iteration in range (60):
    left (45)
    forward (s)
    s = (s + (5/4))

#presun
for action in range (1):
    right (90)
    penup ()
    goto (-100,0)
    pendown ()

#spirala
s = 1
for iteration in range (200):
    left (15)
    forward (s)
    s = (s + (1/10))

# presun + kruh
for action in range (1):
    penup ()
    setposition (20,40)
    pendown ()

speed (-20)
s = 1
for iteration in range (360):
    forward (s)
    left (1)

exitonclick ()
