def ficha(nome='Jogador desconhecido', gols=0):
    print(f'O jogador {nome} fez {gols} gols.')


n = str(input('Digite o nome do jogador: '))
g = str(input('Quantos gols ele marcou? '))
if g.isnumeric():
   g = int(g)
else:
    g = 0
if n.strip() == '':
    n = 'Jogador Desconhecido'
ficha(n, g)
