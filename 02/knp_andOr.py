print("Zahrajeme si?")

tah_cloveka = input('kámen, nůžky, nebo papír? ')
#tah_pocitace = ""

from random import randrange
cislo = randrange(0, 3)

if cislo == 0:
    tah_pocitace = 'kámen'
elif cislo == 1:
    tah_pocitace = "nůžky"
else:
    tah_pocitace = "papír"

if tah_cloveka == "kámen" and tah_pocitace == 'kámen':
        print('Plichta.')
if tah_cloveka == "kámen" and tah_pocitace == 'nůžky':
        print('Vyhrála jsi!')
if tah_cloveka == "kamen" and tah_pocitace == 'papír':
        print('Počítač vyhrál.')
if tah_cloveka == 'nůžky'and tah_pocitace == "nůžky":
        print("Plichta")
if tah_cloveka == 'nůžky'and tah_pocitace == "papír":
        print('Vyhrála jsi!')
if tah_cloveka == 'nůžky'and tah_pocitace == "kámen":
        print('Počítač vyhrál.')
if tah_cloveka == 'papír'and tah_pocitace == "papír":
        print("Plichta")
if tah_cloveka == 'papír'and tah_pocitace == "kámen":
        print('Vyhrála jsi!')
if tah_cloveka == 'papír'and tah_pocitace == "nůžky":
        print('Počítač vyhrál.')
