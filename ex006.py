a = input('Digite algo:')

print('O valor primitivo desse elemento é:', type(a))
print('O valor é númerico?', a.isnumeric())
print('O valor é uma letra?', a.isalpha())
print('O valor só tem espaço?', a.isspace())
print('O valor é decimal?', a.isdecimal())
print('O valor é um dígito?', a.isdigit())
