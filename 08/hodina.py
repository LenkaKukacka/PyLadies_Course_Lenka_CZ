ja = {'jméno': 'Anna', 'město': 'Brno', 'čísla': [3, 7]}
print(ja ['jméno'])

ja['čísla'] = [3, 7, 42] #prepsani, pripsani
print(ja)

#pridat i klic novy
ja['jazyk'] = 'Python'
print(ja)

del ja["město"] #hranate!
print(ja)
#vyuziti, seznamy spojit dvat ypy k sobe, vyhledavaci tabulka - telefonni seznamu
#vyhledavai tabulka - seznamy
#zapis do vice radku, takhle muzes zapsat i seznam a entici
cisla = {
    'Maruška': '153 85283',
    'Terka': '237 26505',
    'Renata': '385 11223',
    'Michal': '491 88047',
}
print(cisla)
barvy = {
    'hruška': 'zelená',
    'jablko': 'červená',
    'meloun': 'zelená',
    'švestka': 'modrá',
    'ředkvička': 'červená',
    'zelí': 'zelená',
    'mrkev': 'červená',
}
print(barvy)

#v cyklech for muzes projet vsechny struktury datove,
#jak ty slovniky prolest
#= for
popisy_funkci = {'len': 'délka', 'str': 'řetězec', 'dict': 'slovník'}
for klic in popisy_funkci:
    print(klic)#anebo metodo keys .keys
#python neni povinny zachovat poradi, jak python necha slovnik v poradi jak jsme jej napsali
#narozdil od seznamu, tam to zustava stejne

#zavolat metodu .values - dostanes hodnoty
for hodnota in popisy_funkci.values():
    print(hodnota)

#pokud potrebujes volat klic i hodnotu, volas entici
#volas entici, zavolat metodu .items
#a print, formatovat jak jej chces dostat
for klic, hodnota in popisy_funkci.items():
    print(klic, hodnota)
#len délka
#str řetězec
#dict slovník
#zavolanim metody .format(co) a predtim Jaky
for klic, hodnota in popisy_funkci.items():
    print('{}: {}'.format(klic, hodnota))

#uvnitr for cyklu nesmis mazat ani pridavat nakresli_domecek
#list na seznam, dict na slovnik
barvy_po_tydnu = dict(barvy)
for klic in barvy_po_tydnu:
    barvy_po_tydnu[klic] = 'černo-hnědo-' + barvy_po_tydnu[klic]
print(barvy['jablko'])
print(barvy_po_tydnu['jablko'])
#dict - vytvoris z jednoho slovniku novy a ten si pak upravis
#pomoci dict prevedes dvojicky (retezce) na slovniku
data = [(1, 'jedna'), (2, 'dva'), (3, 'tři')]
nazvy_cisel = dict(data)
print(nazvy_cisel)
#jiny prevod na slovnik
popisy_funkci = dict(len='délka', str='řetězec', dict='slovník')
print(popisy_funkci['len'])
