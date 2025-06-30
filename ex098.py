from time import sleep

def contador(inicio, fim, passo):
    print(f'Contagem do {inicio} até o {fim} de {passo} em {passo}:')
    if inicio <= fim:
        while inicio <= fim:
            print(inicio, end=' ', flush=True)
            inicio += passo
            sleep(0.4)
    elif passo == 0:
        passo ==1
    elif inicio >= fim:
        while inicio >= fim:
            print(inicio, end=' ', flush=True)
            inicio -= passo
            sleep(0.4)
    print('FIM')
    print('=' * 50)


contador(1, 10, 1)
contador(10, 0, 2)
i = int(input('Digite o valor do início: '))
f = int(input('Digite o valor do Fim: '))
p = int(input('Digite o valor de cada passo: '))
contador(i, f, p)
