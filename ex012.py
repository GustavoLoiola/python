preço = float(input('Digite o preço:'))
desconto = preço -(preço * 5/100)
print('O preço final do produto com 5% de desconto é de: R${:.2f}'.format(desconto))
