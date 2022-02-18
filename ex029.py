velocidade=int(input('Digite a velocidade do seu carro: '))
if velocidade>80:
    multa=velocidade*7
    print('Você foi multado no valor de R${},00(R$7,00*{}) por estar com velocidade acima de 80km/h'.format(multa,velocidade))