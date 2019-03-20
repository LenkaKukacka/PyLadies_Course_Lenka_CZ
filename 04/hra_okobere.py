from random import randrange

soucet = 0
print ("Zahrajes si se mnou Oko bere?")

while soucet <= 21:
    karta = randrange(2,10)
    print ("Karta:" , karta)
    odpoved = input ("Chces pokracovat?")
    soucet = soucet + karta

    if (odpoved == "ne") and (soucet < 21):
        print ("Skoda do 21 zbyvalo:" , 21 - soucet)
        break
    if (odpoved == "ne") and (soucet == 21):
        print ("Vyhrals, vyborne" , soucet)
        break
    if (odpoved == "ne") and (soucet > 21):
        print ("Skoda, presahl. Soucet:" , soucet)
        break

    if (soucet > 21) and (soucet != 21):
        print (soucet)
        print ("Oko bere. Prohrals. Zkus to znova :)")
        break

    #if soucet == 21:
    #print (soucet)
        #rint ("Vyhrals! Vyborne :)")
        #break
