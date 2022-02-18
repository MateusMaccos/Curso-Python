aluno=dict()
aluno['nome']=input('Nome: ')
aluno['média']=int(input(f'A média de {aluno["nome"]} é : '))
if(aluno['média']>=7):
    aluno["situação"]='Aprovado'
else:
    aluno["situação"] = 'Reprovado'

print(f'O nome é igual a {aluno["nome"]}')
print(f'Média igual a {aluno["média"]}')
print(f'Situação igual a {aluno["situação"]}')