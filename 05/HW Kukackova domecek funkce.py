from turtle import pen, speed, setposition, screensize, setup, forward, left, right, down, up, backward, penup, pendown, exitonclick
from math import sqrt

screensize ()
speed (2)

def nakresli_domecek (a, l):
    "Nakresli domecek daneho rozmeru"
    forward (a)
    left (135)
    forward (l)
    right (135)
    forward (a)
    right (135)
    forward (l)
    right (135)
    forward (a)
    right (30)
    forward (a)
    right (120)
    forward (a)
    right (30)
    forward (a)
    left (90)
    forward (10)
a = int(input("zadej vysku domu: "))
l = sqrt((a*a) + (a*a))
nakresli_domecek (a, l)
exitonclick()
