print('Odpovídej "ano" nebo "ne".')
stastna = input('Jsi šťastný/á? ')
bohata = input('Jsi bohatý/á? ')

if stastna == 'ano'and bohata == "ano":
    print('Gratuluji!')
elif stastna == 'ne'and bohata == "ano":
    print('Zkus se víc usmívat.')
elif stastna == "ne" and bohata == "ne":
    print('To je mi líto.')
elif stastna == "ano" and bohata == "ne":
    print('Zkus míň utrácet.')
else:
    print('Nerozumím!')
