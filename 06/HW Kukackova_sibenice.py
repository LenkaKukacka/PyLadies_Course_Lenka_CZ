from random import randrange, random

slovo = randrange(0, 3)

if slovo == 0:
    hadanka = "dum"
if slovo == 1:
    hadanka = "pejsci"
if slovo == 2:
    hadanka = "auto"

pole = "-" * len(hadanka)
print(pole)

uspesny = 0
neuspesny = 0

def vyhodnot(uspesny, neuspesny):
    "Vyhodnotí tah hrace."
    if "-" not in pole:
        print("Vyhrals :)")
        return True
    if neuspesny == -6:
        print("Obesenec. Prohrals. Zkus to znova.")
        return True
    else:
        print("pokracuj")
        return False

def sibenice (neuspesny):
    if neuspesny == -1:
        print("""



        ~~~~~~~""")
    if neuspesny == -2:
        print("""
        +
        |
        |
        |
        |
        |
        ~~~~~~~""")
    if neuspesny == -3:
        print("""
        +---.
        |
        |
        |
        |
        |
        ~~~~~~~""")
    if neuspesny == -4:
        print("""
        +---.
        |   |
        |   O
        | --|--
        |
        |
        ~~~~~~~""")
    if neuspesny == -5:
        print("""
        +---.
        |   |
        |   O
        | --|--
        |  /
        |
        ~~~~~~~""")
    if neuspesny == -6:
        print("""
        +---.
        |   |
        |   O
        | --|--
        |  / \
        |
        ~~~~~~~""")

def tah_hrace (pole, uspesny, neuspesny):
    "Pta se hrace na pismenko, vypise uspesny pokus, obrazek pri neuspesnem, opakuje"
    pismeno = input("Zvol pismeno slova v hadance:")
    pozice = hadanka.find(pismeno)
    print(pozice)
    if pozice >= 0:
        pole = pole[:pozice] + pismeno + pole[pozice + 1:]
        print(pole)
        uspesny = uspesny + 1
        return pole, uspesny, neuspesny #poradil pritel "Python Tuples"
    if pozice < 0:
        print("spatne")
        neuspesny = neuspesny -1
        sibenice(neuspesny)
        return pole, uspesny, neuspesny

while True:
    vysledek = tah_hrace(pole, uspesny, neuspesny)
    print(vysledek)
    pole = vysledek [0] #poradil pritel "Python Tuples"
    uspesny = vysledek [1]
    neuspesny = vysledek [2]
    if vyhodnot(uspesny, neuspesny) == True:
        break

cisla = [1, 2, 3, 4]
cisla[1:-1] = [6, 5]
print(cisla)
