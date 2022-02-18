Frase = input('Digite uma frase: ')

dividido=Frase.split()
teste=''.join(dividido)

print(teste.upper())
n=len(teste)
inverso=''
for c in range(n-1,-1,-1):
    inverso += teste[c]
print(inverso.upper())
if teste.upper() == inverso.upper():
    print('As palavras são palindromos')
else:
    print('As palavras não são palindromos')