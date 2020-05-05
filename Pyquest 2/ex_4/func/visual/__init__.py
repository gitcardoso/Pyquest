def ler_inteiro(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[41mERRO: Por favor, digite um número inteiro válido.\033[m')
            continue
        except (Keyboardinterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def lin(tam = 50):
    return'\033[33m-\033[m' * tam


def cabeçalho(txt):
    print(lin())
    print(txt.center(50))
    print(lin())

def menu(lista):
    cabeçalho('\033[36mPYQUEST FASE 2 - EXERCÍCIO 4\033[m')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(lin())
    opc = ler_inteiro('\033[31mSua opção: \033[m')
    return opc
