def ficha(nome='<desconhecido>',gols='0'):
    """
    -> Recebe o nome de um jogador e quantos gols ele marcou, após isso ele mostra a ficha do jogador
    :param nome: Nome do jogador
    :param gols: quantos gols ele fez
    :return: nenhum
    """
    print(f'Nome do Jogador: {nome}')
    print(f'Número de gols: {gols}')
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


#Principal
n=input('Nome do Jogador: ')
g=input('Quantidade de gols: ')
if(n=='' and g!=''):
    ficha(gols=g)
elif(g=='' and n!=''):
    ficha(nome=n)
elif(g=='' and n==''):
    ficha()
else:
    ficha(n,g)






