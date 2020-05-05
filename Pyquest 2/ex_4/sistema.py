'''Faça um programa em Python utilizando os conceitos
de manipulação de arquivos para armazenar
o nome e o telefone de um grupo de pessoas.
O programa deve ser capaz de exibir a lista de pessoas com seus respectivos dados'''

from func.visual import *
from func.arq import *
from time import sleep


arq = 'cadastropessoas.txt'

if not arq_existe(arq):
    criar_arq(arq)



while True:
    res = menu(['Ver cadastro', 'Cadastrar pessoas', 'Sair'])
    if res == 1:
        # opção de listar o conteúdo de um arq
        ler_arq(arq)
    elif res == 2:
        # opção de cadastrar um nova pessoa
        cabeçalho('\033[34mNOVO CADASTRO\033[m')
        nome = str(input('Nome: '))
        telefone = ler_inteiro('Telefone: ')
        cadastrar(arq, nome, telefone)
    elif res == 3:
        # opção de sair do sistema
        cabeçalho('Cadastro finalizado')
        break
    else:
        # digitou uma opção errada no menu
        cabeçalho('\033[41mERRO! Digite uma opção válida!\033[m')
    sleep(2)
