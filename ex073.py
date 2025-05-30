print('--------------- TABELA DO BRASILEIRÃO --------------- ')

tabela = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Bragantino', 'Fluminense', 'Ceará', 'Bahia', 'Corinthians' ,'Mirassol', 'Atlético-MG', 'Botafogo', 'Grêmio', 'São Paulo', 'Internacional', 'Vasco', 'Fortaleza', 'Vitória', 'Santos', 'Juventude', 'Sport')

print(tabela)
print(f'G6 do Brasileirão: {tabela[:6]}')
print(f'Z4 do Brasileirão: {tabela[-4:]}')
print(f'Times em ordem alfabética: {sorted(tabela)} ')
print(f'O Vasco da Gama está em {tabela.index('Vasco')+1}° lugar')
