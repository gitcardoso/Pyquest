from func.visual import *

def arq_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arq!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def ler_arq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arq!')
    else:
        cabeçalho('\033[34mPESSOAS CADASTRADAS\033[m')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3}')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', telefone=0 ):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arq!')
    else:
        try:
            a.write(f'{nome};{telefone}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'{nome} cadastrado(a) com sucesso!')
            a.close()
