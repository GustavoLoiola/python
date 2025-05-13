from datetime import date
ma = 0
me = 0
for c in range(1, 8):
    nas = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    idd = date.today().year - nas
    if idd >= 18:
        ma += 1
    elif idd < 18:
        me += 1
print('{} Pessoas são maiores de idade e {} Pessoas são menores de idade.'.format(ma,me))
