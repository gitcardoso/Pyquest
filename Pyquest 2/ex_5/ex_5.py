'''Faça um programa em Python utilizando os conceitos
de orientação a objetos para armazenar o nome,
a idade, a altura e o peso de uma pessoa.
Ao final o programa deve exibir os dados da pessoa
e seu índice de massa corporal (IMC).
O IMC é calculado dividindo o peso pela altura elevada ao quadrado.
Ou seja, de forma mais simples, você multiplica sua altura por ela mesma
e depois divide seu peso pelo resultado da última conta'''

from ex_5Classe import Pessoa

print('-' * 50)
print('TESTE DE MASSA CORPORAL (IMC)'.center(50))
print('-' * 50)

nome = str(input('Digite o nome da pessoa: '))
idade = int(input('Digite a idade da pessoa: '))
altura = float(input('Digite a altura da pessoa: '))
peso = float(input('Digite o peso da pessoa: '))


p1 = Pessoa(nome, idade, altura, peso)

print('-' * 50)
print('RESULTADO'.center(50))
print('-' * 50)
p1.mostra()
print('-' * 50)
p1.imc()
print('=' * 50)
