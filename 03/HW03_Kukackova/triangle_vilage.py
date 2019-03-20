# triangle
from turtle import pen, speed, setposition, screensize, setup, forward, left, right, down, up, backward, penup, pendown, exitonclick, shape
screensize ()
setup (width = 1.0, height = 1.0)

shape ("turtle")
pen (fillcolor = "red", pensize = 2)
speed (0.5)

for action in range (1):
    penup ()
    setposition (-600,250)
    pendown ()

for action in range (3):
    forward (150)
    left (120)

for action in range (1):
    penup ()
    right (90)
    forward (250)
    left (90)
    pendown ()

#houserow
pen (fillcolor = "red", pensize = 2)
for action in range (11):
    forward (100)
    left (135)
    forward (141)
    right (135)
    forward (100)
    right (135)
    forward (141)
    right (135)
    forward (100)
    right (30)
    forward (100)
    right (120)
    forward (100)
    right (30)
    forward (100)
    left (90)
    #penup ()
    forward (10)
    #pendown ()

#presun
for action in range (1):
    penup ()
    setposition (-600,-200)
    pendown ()

#mnohouhelniky
for iteration in range (5):
    n = 5 + iteration
    s = 100 - (10 * iteration)

    for angle in range (n):
        forward (s)
        left (180 - (180 * (1 - 2/n)))

    penup ()
    forward (200)
    pendown ()

#Kolecko
s = 5
for angle in range (100):
    forward (s)
    left (180 - (180 * (1 - 2/100)))

#zadani n uzivatelem
for action in range (1):
    penup ()
    setposition (-500,-350)
    pendown ()

#zadani uzovatelem/95uhelnik
n = int(input ("ted zadej počet úhlu ty:"))
s = 50 - (2*n)
for angle in range (n):
    forward (s)
    left (180 - (180 * (1 - 2/n)))
exitonclick ()
