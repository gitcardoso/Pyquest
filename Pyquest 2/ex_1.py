"""Faça um programa em Python utilizando os conceitos
de listas e dicionário para armazenar o
código, o nome, a altura e a idade de um grupo de pessoas.
Ao final o programa deve exibir a quantidade de pessoas,
a média das idades e a média das alturas das pessoas."""

dados = {}
pessoas = []
somaidade = mediaidade = 0
somaalt = mediaalt = 0

while True:
    dados.clear()
    dados['codigo'] = int(input('Digite o código da pessoa: '))
    dados['nome'] = str(input('Digite o nome da pessoa: '))
    dados['altura'] = float(input('Digite a altura da pessoa: '))
    somaalt += dados['altura']
    dados['idade'] = int(input('Digite a idade da pessoa: '))
    somaidade += dados['idade']
    pessoas.append(dados.copy())
    while True:
        res = str(input('Quer continuar? [S/N]')).upper()[0]
        if res in 'SN':
            break
        print('Digite apenas S ou N')
    if res == 'N':
        break
print('-' * 50)
print(f'No total são {len(pessoas)} pessoas armazenadas.')
mediaidade = somaidade / len(pessoas)
print(f'A média das idades é: {mediaidade:5.2f}')
mediaalt = somaalt / len(pessoas)
print(f'A média das alturas é: {mediaalt:5.2f}')





