def obvod_obdelnika(sirka, vyska):
    "Vrátí obvod obdélníka daných rozměrů"
    return 2 * (sirka + vyska)

print(obvod_obdelnika(4, 2))

from math import pi

def obsah_elipsy(a , b):
    "vrati obsah elipsy"
    return pi *(a * b)
print("Obsah elipsy s osami 4 a 2 cm je" , obsah_elipsy(4,2) , "cm2")

def nic():
    "Tahle funkce nic nedělá"

print(nic()) #pouziti, mas funkci v kodu, ktera nic nevraci

print('--\N{LATIN SMALL LETTER L WITH STROKE}--')
print('--\N{SECTION SIGN}--')
print('--\N{PER MILLE SIGN}--')
print('--\N{BLACK STAR}--')
print('--\N{SNOWMAN}--')
print('--\N{KATAKANA LETTER TU}--')

print("""Haló haló!
Co se stalo?
Prase kozu potrkalo!""")

pate_pismeno = 'čokoláda'[-5]

print(pate_pismeno)
#vsechno zacina na nulo!!!!

jmeno = input("Napis vlastni jmeno:")
prijmeni = input("Napis sve prijmeni:")
inicial1 = jmeno [0]
inicial2 = prijmeni [0]
print("Tve inicialy jsou:", inicial1.upper()+inicial2.upper())

vypis = '{}×{} je {}'.format(3, 4, 3 * 4)
print(vypis)

vypis = 'Ahoj {jmeno}! Výsledek je {cislo}.'.format(cislo=7, jmeno='Elvíro')
print(vypis)
