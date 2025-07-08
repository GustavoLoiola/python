import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.google.com/?hl=pt-BR')
except:
    print('\033[31mO site está indisponível no momento.\033[m')
else:
    print('O site está acessível no momento atual!')

finally:
    print('Volte sempre!')
