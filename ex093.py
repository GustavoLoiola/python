est = dict()
tot = 0

est['Nome'] = str(input('Digite o nome do jogador: '))
est['Partidas'] = int(input('Digite quantas partidas ele jogou: '))
Partidas = est['Partidas'] 
Partidas = []
for c in range(est['Partidas']):
     g = int(input(f'Quantos gols ele marcou na {c+1}° partida? '))
     Partidas.append(g) 
     tot += g
est['Gols'] = Partidas
est['Total'] = tot
print('=+'*55)
print(est)
print('=+'*55)
for k, v in est.items():
   print(f'O campo {k} tem valor {v}')
print('=+'*55)
print(f'O jogador {est['Nome']} jogou {est["Partidas"]} partidas')
num = 0
for c in range(est['Partidas']):
    print(f'Na partida {c +1}, fez {Partidas[num]} gols')
    num += 1
print('=+'*55)
