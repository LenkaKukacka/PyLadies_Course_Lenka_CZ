from random import randrange
print("Zadej postupne tri cisla:")
a = int(input ("cislo 1:"))
b = int(input ("cislo 2:"))
c = int(input ("cislo 3:"))
soucet = (a + b + c)
print("Jaky je jejich soucet?")
if soucet < 100:
    print(soucet , "...Soucet je mensi nez 100.")
elif soucet == 100:
    print(soucet , "...Trefils pesne 100.")
else:
    print(soucet , "...Tak je to pres stovku.")

#sude liche
cislo = int(input ("Zadej cislo:"))
if cislo%2 == 0:
    print("cislo je sude")
elif cislo%2 == 1:
    print("cislo je liche")
print(" ")

#bumbac
print("Hra bum-bac")
for n in range (1,101):
    if n%3 == 0:
        print("bum" , end=" ")
    elif n%5 == 0:
        print("bac" , end=" ")
    elif (n%3 == 0) and (n%5 == 0):
        print("bumbac" , end=" ")
    else: #(n%3 !=0) or (n%5 !=0):
        print(n , end=" ")
