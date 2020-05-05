"""Faça um programa em Python utilizando os conceitos
de listas e dicionário para armazenar o código,
o nome e o preço de um grupo de produtos.
Ao final o programa deve exibir o valor médio dos produtos
e os nomes dos produtos com preço superior a média do grupo"""


produto = {}
cadastro = []
somapreco = mediapreco = 0

while True:
    produto.clear()
    produto['codigo'] = int(input('Digite o código do produto: '))
    produto['nome'] = str(input('Digite o nome do produto: '))
    produto['preco'] = float(input('Digite o preço do produto: '))
    somapreco += produto['preco']
    cadastro.append(produto.copy())
    while True:
        res = str(input('Quer continuar? [S/N]')).upper()[0]
        if res in 'SN':
            break
        print('Digite apenas S ou N')
    if res == 'N':
        break
print('-' * 50)

mediapreco = somapreco / len(cadastro)
print(f'O valor médio dos produtos é: {mediapreco:5.2f}')
print(f'Os produtos com o preço superior à média são: ', end='')
for p in cadastro:
    if p['preco'] > mediapreco:
        print(p['nome'], end='. ')
