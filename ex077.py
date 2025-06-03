palavras = ('Gustavo', 'Gabriela', 'Alcion', 'Idalia', 'Samuel', 'Saulo', 'Cleide', 'Nubia', 'Adiel', 'Leo', 'Matehus', 'Vivian')

for p in (palavras):
    print(f'\nNa palavra {p.upper()} encontramos as vogáis ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')
