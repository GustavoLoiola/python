s1 = int(input('Digite o valor do primeiro seguimento: '))
s2 = int(input('Digite o valor do segundo seguimento: '))
s3 = int(input('Digite o valor do terceiro seguimento: '))

if s1 < s2 + s3 and s2 < s3 + s1 and s3 < s1 + s2:
    print('Esses seguimentos podem formar um triângulo!')

else:
    print('Esses valores NÃO podem formar um triângulo!')
