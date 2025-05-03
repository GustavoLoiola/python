p = float(input('Digite o valor da sua compra: R$'))

print('Digite a forma de pagamento.')
print('[1] Dinheiro / Pix')
print('[2] À vista no cartão')
print('[3] Até 4x no cartão')
print('[4] Acima de 4x no cartão')
op = int(input('Forma de pagamento: '))

if op == 1:
    print('O valor da sua compra é de R${:.2f}'.format(p - (p *10/100)))

elif op == 2:
    print('O valor da sua compra é de RS{:.2f}'.format(p - (p *5/100)))

elif op == 3:
    par = int(input('Quantas parcelas?'))
    if par >=1 and par <=4:
      print('O valor da sua compra é de R${:.2f}, que deverá ser pago em {} parcelas de R${:.2f}'.format(p, par, (p/ par)))
    else:
        print('Número inválido!')

elif op == 4:
    par = int(input('Digite a quantidade de parcelas: '))
    if par >=5 and par <=12:
      valjuros = p + (p *20/100)
      print('O valor da sua compra é de R${:.2f}, que deverá ser pago em {} parcelas de R${:.2f}'.format(valjuros, par, valjuros / par  ))
    else:
        print('Número inválido!')
else: 
    print('Opção inválida!')
