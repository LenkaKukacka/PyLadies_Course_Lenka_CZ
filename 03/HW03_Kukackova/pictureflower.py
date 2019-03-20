# triangle
import turtle
from turtle import pen, speed, setposition, screensize, setup, goto, forward, left, right, down, color, up, backward, penup, filling, pendown, exitonclick, shape

screensize ()
setup (width = 1.0, height = 1.0)
colors = ["red", "orange", "green", "cyan", "blue", "purple", "magenta", "pink", "brown"]
shape ("turtle")
pen (fillcolor = "red", pensize = 2)
speed (0)
penup ()
x = -500
y = 200
setposition (x,y)
#natoceni
left (225)
pendown ()

color ("red")

for i in range (18):
    for akce in range (4):
        forward(50)
        left(90)
    left (20)

color ("green")
speed (0)
left (45)
penup ()
forward (200)
pendown ()

right (150)
n = 1
for i in range (100):
    forward (n)
    left (1)

left (80)

for i in range (100):
    forward (n)
    left (1)

left (40)
n = 0.5
for i in range (100):
    forward (n)
    right (1)

right (80)

n = 0.5
for i in range (100):
    forward (n)
    right (1)

pensize = 4
right (70)
forward (200)


penup ()
setposition (100,300)
pendown ()
left (180)
#forward (300)

penup ()
x = 100
y = 0
setposition (x - 10,y + 10)
right (115)
pendown ()

for i in range (5):
    n = 1
    for i in range (100):
        forward (n)
        left (1)
    left (80)
    for i in range (100):
        forward (n)
        left (1)

    penup ()
    setposition (x - 10, y + 40)
    pendown ()
exitonclick ()
