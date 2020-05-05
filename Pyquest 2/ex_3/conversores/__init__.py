def conv_dol(a):
    b = 5.41
    print(f'O valor convertido em Dolar é: \t{a / b:.2f}'.replace('.', ','))


def conv_eur(a):
    b = 5.85
    print(f'O valor convertido em Euro é: \t{a / b:.2f}'.replace('.', ','))


def conv_lib(a):
    b = 6.66
    print(f'O valor convertido em Libra é: \t{a / b:.2f}'.replace('.', ','))


def cabeçalho():
    print('\n')
    print('=' * 50)
    print('<<CONVERSOR DE MOEDAS>>'.center(50))
    print('=' * 50)