def metade(x=0, format=False):
    res=x/2
    return res if format is False else moeda(res)
def dobro(x=0, format=False):
    res = 2*x
    return res if format is False else moeda(res)
def aumentar(x=0,y=0, format=False):
    aumento=x*(y/100)+x
    return aumento if format is False else moeda(aumento)
def diminuir(x=0,y=0,format=False):
    decrescimo=x-(x*(y/100))
    return decrescimo if format is False else moeda(decrescimo)

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')

def resumo(preço=0, aumento=10, redução=5):
    print('-'*35)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 35)
    print(f'PREÇO ANALISADO: {moeda(preço)}'.center(30))
    print('-' * 35)
    print(f'O dobro de {moeda(preço)}: \t{dobro(preço, True)}')
    print(f'A metade de {moeda(preço)}: \t{metade(preço, True)}')
    print(f'Aumento de {aumento}%: \t\t{aumentar(preço, aumento, True)}')
    print(f'Redução de {redução}%:  \t\t{diminuir(preço, redução, True)}')
    print('-' * 35)