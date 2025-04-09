import math
ang = int(input('Digite um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O ângulo {}° tem o Seno de {:.2f}, o Cosseno de {:.2f} e a Tangente de {:.2f}'.format(ang, sen, cos, tan))
