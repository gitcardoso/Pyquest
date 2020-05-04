"""Faça um programa que leia dois números e mostre qual o maior dos dois.
O programa deve informar caso sejam iguais."""

num1 = float(input('Digite o primeiro número:'))
num2 = float(input('Digite o segundo número:'))
if num1 > num2:
    print('O número {} é maior que o número {}'.format(num1, num2))
elif num2 > num1:
    print('O número {} é maior que o número {}'.format(num2, num1))
else:
    print('Os números {} e {} são iguais'.format(num1, num2))
