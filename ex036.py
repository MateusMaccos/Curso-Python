casa=int(input('\033[4;37;40mQual o valor da sua casa? '))
salario=int(input('\033[0;32;44mQual o seu salário? '))
anos=int(input('\033[0;32;44mEm quantos anos você vai pagar? '))
prestação = casa/(anos*12)
if prestação > 0.3*salario:
    print('Empréstimo Negado')
else:
    print('Empréstimo Aceito')
