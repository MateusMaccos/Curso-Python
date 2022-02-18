def leiaint(msg):
    while True:
        try:
            Inteiro = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERROR! DIGITE UM NÚMERO INTEIRO VÁLIDO!\033[m')
        except(KeyboardInterrupt):
            print('\033[31mERROR! O USUÁRIO PREFERIU NÃO DIGITAR NADA!\033[m')
        else:
            return Inteiro
def leiafloat(msg):
    while True:
        try:
            Real = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERROR! DIGITE UM NÚMERO REAL VÁLIDO!\033[m')
        except(KeyboardInterrupt):
            print('\033[31mERROR! O USUÁRIO PREFERIU NÃO DIGITAR NADA!\033[m')
        else:
            return Real


i=leiaint('Digite um número inteiro: ')
f=leiafloat('Digite um número real: ')
print(f'O número inteiro digitado foi {i} e o real foi {f}')