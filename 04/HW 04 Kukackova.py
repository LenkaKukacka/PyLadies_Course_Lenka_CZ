from random import randrange

#4xa a radky
for a in range (4):
    print("a")

print("")

cislo = 0
for cislo in range (5):
    print("Řádek" , " " , cislo)
    cislo = cislo + 1
print("")

#promenna = Cislo
cislo = 0
for cislo in range (5):
    vysledek = cislo **2
    print(cislo , "na druhou je" , vysledek)

for j in range (5):
    print("")
    for i in range (5):
        print("x" , end=" ")
print(" ")
print(" ")

#nasobilka
cislo = 0
for j in range (5):
    for i in range (5):
        cislo = (j*i)
        print (cislo , end=" ")
    print(" ")
#Xka
for i in range (4):
    for j in range (4):
        if i >= j:
            print("X" , end=" ")
        else:
            print(" " , end=" ")
    print(" ")

#prvni radek
for i in range (1):
    for j in range (4):
        if i >= j:
            print("prvni radek")
        else:
            print("neni prvni")
    print(" ")

#ctverect z X
min = 0
limit = 5
for i in range (limit + 1):
    for j in range (limit + 1):
        if ((i == limit) or (i == min)) or ((j == limit) or (j == min)):
            print("X" , end=" ")
        else:
            print(" ", end=" ")
    print(" ")

#zadani uzivatelem
min = 0
limit = int(input ("Zadej pocet radku:"))
for i in range (limit + 1):
    if (limit > 0 and limit < 100):
        for j in range (limit + 1):
            if ((i == limit) or (i == min)) or ((j == limit) or (j == min)):
                print("X" , end=" ")
            else:
                print(" ", end=" ")
        print(" ")
        
    else:
        print("Zkus zadat cislo od 1 do 100.")
print(" ")
