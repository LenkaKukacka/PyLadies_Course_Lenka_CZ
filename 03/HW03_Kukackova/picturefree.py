# triangle
import turtle
from turtle import pen, speed, setposition, screensize, setup, goto, forward, left, right, down, color, up, backward, penup, filling, pendown, exitonclick, shape

screensize ()
setup (width = 1.0, height = 1.0)
colors = ["red", "orange", "green", "cyan", "blue", "purple", "magenta", "pink", "brown"]
shape ("turtle")
pen (fillcolor = "red", pensize = 2)
speed (3)
penup ()
x = -500
y = 200
setposition (x,y)
#natoceni
left (225)
pendown ()

shape ("triangle")
color ("green")

for i in range (5):
    n = 50
    s = 70
    p = 40
    for triangle in range (3):
        forward (n)
        left (180 - 45)
        forward (s)
        right (180 + 45)
        forward (n)
        left (135)
        penup ()
        forward (p)
        right (45)
        pendown ()
        n = 50 + (1/2 * n)
        s = 70 + (1/2 * s)
        p = 40 + (1/2 * p)
    penup ()
    x = x + 150
    setposition (x,y)
    pendown ()
exitonclick ()
