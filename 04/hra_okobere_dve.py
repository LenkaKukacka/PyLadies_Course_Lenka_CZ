from random import randrange

soucet = 0
#odpoved = ("ano", "ne")

while True:
    karta = randrange(2,10)
    print ("Karta:" , karta)
    soucet = soucet + karta
    #print (soucet)
    if soucet > 21:
        print (soucet)
        print ("Oko bere. Prohrals. Zkus to znova :))")
        break

    odpoved = input ("Chces pokracovat?")

    if odpoved == "ne":
        print ("Soucet:" , soucet)
        break
