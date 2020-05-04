"""Faça um programa que dado o valor da temperatura em graus FARENHEIT, calcular e escrever o valor da temperatura em graus CELSIUS.
Fórmula: C = 5/9 * (F - 32)"""

f = int(input('Digite a temperatura em graus FARENHEIT:'))
c = 5/9 * (f - 32)
print('A temperatur em graus Celsius é: {}°'.format(int(c)))

