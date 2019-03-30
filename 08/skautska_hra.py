import random

otazky = ["Kdo?", "S kým?", "Co dělali?" , "Kde?" , "Kdy?" , "Proč?"]

def ptej_se (otazky):
    odpovedi = []
    for otazka in otazky:
        odpoved = input(otazka)
        odpovedi.append(odpoved)
    return(odpovedi)

def sesbirej():
    seznam_odpovedi = []
    for x in range (3):
        seznam_odpovedi.append(ptej_se(otazky))
    return(seznam_odpovedi)

def pomichej(seznam_odpovedi):
    veta = " "
    for x in range (len(otazky)):
        y = random.randrange(len(seznam_odpovedi))
        odpovedi = seznam_odpovedi[y]
        slovo = odpovedi[x]
        veta = veta + " " + slovo
    print(veta)
pomichej(sesbirej())
