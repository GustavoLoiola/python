print('---------- SEQUÊNCIA DE FIBONACCI ----------')
tm = int(input('Quantas sequências você deseja mostrar? '))
fib1 = 0
fib2= 1
print('{} -> {}'.format(fib1, fib2), end=' ')
pt = 3
while pt <= tm:
    fib3 = fib1 + fib2
    print('-> ',fib3, end=' ')
    pt += 1
    fib1 = fib2
    fib2 = fib3
print('-> FIM')
    