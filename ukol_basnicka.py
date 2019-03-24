#9 otoceni basnicky
with open("basnicka.txt" , encoding="utf-8") as soubor:
    basnicka = list(soubor)#prevod na list nefunguje
    basnicka.reverse()
print(basnicka)

# 10
