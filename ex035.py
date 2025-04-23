s1 = int(input('Digite o valor do primeiro seguimento: '))
s2 = int(input('Digite o valor do segundo seguimento: '))
s3 = int(input('Digite o valor do terceiro seguimento: '))

if s1 < s2 + s3 and s2 < s3 + s1 and s3 < s1 + s2:
    print('\033[1;42;33mEsses seguimentos podem formar um triângulo!\033[m')

else:
    print('\033[1;41;33m Esses valores NÃO podem formar um triângulo!\033[m')
