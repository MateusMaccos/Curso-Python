nome = input('Qual seu nome completo? ')

nomes = nome.split()
print('O nome da pessoa com maiusculas: {}'.format(nome.upper()))
print('O nome da pessoa com minusculas: {}'.format(nome.lower()))
print('O nome completo da pessoa tem {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(len(nomes[0])))
