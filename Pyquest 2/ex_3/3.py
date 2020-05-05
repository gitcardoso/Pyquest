from conversores import conv_dol, conv_eur, conv_lib, cabeçalho

real = float(input('Digite o valor em Reais para ser convertido R$:'))
cabeçalho()
conv_dol(real)
conv_eur(real)
conv_lib(real)
print('-' * 50)
