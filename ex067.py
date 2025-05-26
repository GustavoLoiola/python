while True:
        num = int(input('Digite um número para ver a sua taboada (número negativo para finalizar): '))
        if num <0:
          print('PROGRAMA ENCERRADO')
          break
        cont = 1
        while cont < 11:
            print('-'*50)
            print(f'{num} x {cont} = {num*cont}')
            cont +=1
