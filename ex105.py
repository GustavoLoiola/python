def notas(*prova, sit=False):
    """Função para analisar as notas de uma sala de aula.
    *prova = campo a ser preenchido com as notas.
    sit=False(padrão) não mostra a situação da sala.
    sit=True mostra a opnião sobre a situação da sala."""
    maior = max(prova)
    menor = min(prova)
    soma = 0
    qnt = len(prova)
    for prova in prova:
        soma += prova
        media = soma / qnt
    dic = {'Total': qnt, 'Maior': maior, 'Menor': menor, 'Media': media}
    for k, v in dic.items():
        print(f'O campo {k} tem valor: {v}')
    if sit == True:
        if dic['Media'] >= 7:
            print('Situação ótima!')
        elif dic['Media'] >= 4:
            print('Situação delicada!')
        else:
            print('Situação péssima!')


notas(4, 5, 6, 0, 0, 2, 5, 3, sit=True)
help(notas)
