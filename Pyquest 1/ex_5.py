"""Crie um programa que leia a altura de 10 pessoas.
Ao final o programa deve informar o total de pessoas cadastradas,
a quantidade de pessoas com altura inferior a 1,60 metros;
a quantidade de pessoas com altura entre 1,60 metros e 1,80 metros
e a quantidade de pessoas com altura superior a 1,80 metros."""

b = m = a = 0
for c in range(10):
    altura = float(input('Digite a altura:'))
    if altura < 1.6:
        b += 1
    elif altura > 1.8:
        a += 1
    else:
        m +=1
else:
    print('10 pessoas foram cadastradas')
    print('existem {} pessoas menores que 1.6m, {} pessoas entre 1.6m e 1.8m e {} pessoas maiores que 1.8m'
          .format(b, m, a))
