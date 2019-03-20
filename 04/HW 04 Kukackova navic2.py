from random import randrange
from math import factorial

#jak sem k tomu probuh dosla? .. google :D
n = int(input ("Zadej cislo, dostanes jeho faktorial:"))
num = 1
for i in range (n,0,-1):
    num = num * i
    #print(num)
print(num)

#prvocilo je delitelen 1 a samosebou, neni to 1
print("tve cislo ...")
if (n%1 == 0) and (n%n == 0):
    print("ano, toto cislo je prvocislo")
else:
    print("nope, to neni prvocislo")

#fibonacciho posloupnos - vzdavam to :)
#or i in range (n,-1,-2):
    #if n >= 0:
        #num = num + i
        #print(num , end=" ")

pocet = 20
a = 0
b = 1

print(a, b, sep=", ", end=", ")

for i in range(pocet):
    dalsi_v_rade = a + b
    a = b
    b = dalsi_v_rade

    print(dalsi_v_rade, end=", ")
