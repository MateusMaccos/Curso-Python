numero = int(input('Digite um número: ')) #1000a + 100b+ 10c + d =
unidade = int(numero/1 %10)
dezena = int(numero/10 %10)
centena = int(numero/100 %10)
milhar = int(numero/1000 %10)
print('milhar: {}',format(milhar))
print('centena: {}',format(centena))
print('dezena: {}',format(dezena))
print('unidade: {}',format(unidade))