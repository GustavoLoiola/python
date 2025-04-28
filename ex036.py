casa = float(input('Digite o valor do imóvel em reais: R$'))
salario = float(input('Digite o seu salário atual em reais: R$'))
anos = float(input('Em quantos anos o imóvel será pago? '))
meses = anos * 12
parcela = casa / meses

print('Para financiar um imóvel no valor de R${:.2f} serão necessárias {:.0f} parcelas de R${:.2f}'.format(casa, meses, parcela))

if parcela > salario - (salario * 70 / 100):
    print('O valor é muito alto para o seu faturamento atual.')
    print('\033[1;31mEMPRÉSTIMO NEGADO!\033[m')

else: 
    print('Os valores condizem com o seu faturamento, obrigado pela escolha!')
    print('\033[1;32mEMPRÉSTIMO ACEITO!\033[m')
