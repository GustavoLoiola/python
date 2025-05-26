from random import randint
print('VAMOS JOGAR PAR OU ÍMPAR!')
vit = 0

while True:
    esc = str(input('PAR ou ÌMPAR [P/I]: ')).upper()
    if esc != 'P' or 'I':
        print('Letra inválida!')
    num = int(input('Digite um número: '))
    pc = randint(0, 10)
    print(f'Minha escolha: {pc}')
    
    if esc == 'P':
        if (pc + num) % 2 ==0:
            print('VOCÊ GANHOU!')
            vit += 1
        else:
            print('VOCÊ PERDEU!')
            break

    if esc == 'I':
        if (pc + num) % 2 ==0:
            print('VOCÊ PERDEU!')
            break
        else:
            print('VOCÊ GANHOU!')
            vit += 1

print(f'Você ganhou {vit}x antes de perder')
