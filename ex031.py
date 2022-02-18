ano= int(input('digite um ano para saber se ele é bissexto: '))
bissexto=ano%4
if bissexto==0:
    print('{} é bissexto'.format(ano))
else:
    print('{} não é bissexto'.format(ano))