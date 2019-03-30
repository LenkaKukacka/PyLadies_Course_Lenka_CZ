#0
def mocniny_dvou (n):
    "Funkce projede radu od 1 do n a vytvori slovnik, kde klic bude cislo, hodnota druha mocnina cisla"
    seznam = [(x, x**2) for x in range(1, n+1)]
    slovnik = dict(seznam)
    print(slovnik)
    return(slovnik)
mocniny_dvou(20)

#1
def soucet_klicu_a_hodnot (n):
    "sečte a vrátí sumu všech klíčů a sumu všech hodnot ve slovníku, který dostane jako argumen"
    seznam = [(x, x**2) for x in range(1, n+1)]
    slovnik = dict(seznam)
    soucet_klicu = sum(slovnik.keys())
    soucet_hodnot = sum(slovnik.values())
    print((soucet_klicu, soucet_hodnot))
soucet_klicu_a_hodnot(20)

#2
veta = input(("Napis svuj oblibeny pozdrav:"))
def pocet_znaku (veta):
    seznam_znaku = list(veta) #seznam po znacich
    seznam_2 = [(x, seznam_znaku.count(x)) for x in seznam_znaku]
    print(seznam_2)
    slovnik = dict(seznam_2)
    print(slovnik)
pocet_znaku(veta)

#3
def vypis_slovniku (ble):
    #barvy = {"1": "cervena", "2": "zelena", "3": "modra"}
    for klic, hodnota in ble.items():
        print('Klic {}, hodnota {}'.format(klic, hodnota))
vypis_slovniku(mocniny_dvou(20))
