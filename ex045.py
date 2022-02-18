
import time
from random import randint
Lista = ['Pedra','Papel','Tesoura']
Jogada = int(input('Sua opções:\n[0]Pedra\n[1]Papel\n[2]Tesoura\nQual é sua jogada?'))
Jogador = Lista[Jogada]
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
Sorteado= randint(0,2)
Computador=Lista[Sorteado]
print('======================')
print('Computador jogou {}'.format(Computador))
print('Vc jogou {}'.format(Jogador))
print('======================')
if Jogador == 'Pedra' and Sorteado == 2:
    print('JOGADOR GANHOU')
elif Jogador == 'Papel' and Sorteado == 0:
    print('JOGADOR GANHOU')
elif Jogador == 'Tesoura' and Sorteado == 1:
    print('JOGADOR GANHOU')
elif Jogador == Computador:
    print('Empate')
else:
    print('COMPUTADOR GANHOU')
