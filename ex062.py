print('---------- Progressão Aritmética ----------')
pt = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
cont = 1
total = 0
mais  =10
while mais != 0:
    total += mais
    while cont <= total:
        print(pt, end=' -> ')
        pt += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer ver mais? (0 para encerrar): '))


if mais == 0:
    print('Você terminou a sua progressão artitmética com {} termos visualizados.'.format(total))
