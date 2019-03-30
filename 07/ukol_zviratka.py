zviratka = ["pes", "kocka", "kralik", "had"]
print(zviratka)
#1
def mensi ():
    vysledek = []
    for zvire in zviratka:
        #delka = len(zvire)
        if len(zvire) <= 5:
            vysledek.append(zvire)
    return vysledek

print(mensi())
#2
def prvni_pismeno ():
    vysledek = []
    for zvire in zviratka:
        ka = zvire[0]
        if ka == "k": #je dobre ze ji mam uvnitr funkce, lokalni
            vysledek.append(zvire)
    #return vysledek #neni nutny, pokud nechci hodnotu vratit z funkce
    #moje funkce by ale nesla pouzit nezavisle na argumentu! jinak
    #startswith/endswith a azve volani funkce zavolam argument pismeno = k
print(prvni_pismeno()) #nema tu byt print vysledek?
#3
def hledej ():
    "prohleda seznam a vypise, pokud hledane slovo na seznamu je, ci neni"
    slovo = input("Napis domaci zvire:")
    if slovo in zviratka:
        print("Ano" , slovo , "je na seznamu.")
    else:
        print("Ne" , slovo , "neni na seznamu.")
        #return slovo in zviratka   abud eto stacit!
hledej()

#4
dalsi_zviratka = ["pavouk", "mys", "andulka", "morcatko"]

def mnoziny ():
    spojene = zviratka + dalsi_zviratka
    print("Dohromady:" , spojene)
    oddelene = zviratka, dalsi_zviratka
    print("Zvlast:" , oddelene)
    druhy = dalsi_zviratka
    print("Druhy seznam:" , dalsi_zviratka)
mnoziny()

#5 serazeni podle abcdef
zviratka.extend(dalsi_zviratka)
zviratka.sort()
print("Seradime to:" , zviratka)

#6 bez 0 - nefunguje
a = ['andulka', 'had', 'kocka', 'kralik']
a.sort(key=lambda x:x[-2])
print(a)
