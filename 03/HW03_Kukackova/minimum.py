minimum = 0
for x in range(5):
    cislo = int(input('Zadej cislo: '))

    if minimum == 0 or cislo < minimum:
        minimum = cislo
print('Nejmensi zadane cislo je', minimum)
