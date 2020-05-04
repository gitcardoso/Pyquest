"""Faça um programa para solicitar o nome e as duas notas de um aluno.
Calcular sua média e informá-la.
Se ela for inferior a 7, escrever "Reprovado”; caso contrário escrever "Aprovado"."""

aluno = str(input('Digite o nome do aluno:'))
nota1 = float(input('Digite a primeira nota do aluno {}:'.format(aluno)))
nota2 = float(input('Digite a segunda nota do aluno {}:'.format(aluno)))
media = (nota1 + nota2)/2
if media >= 7:
    print('A média do aluno {} é:{}'.format(aluno, media))
    print('O aluno {} foi aprovado, parabéns!'.format(aluno))
else:
    print('A média do aluno {} é: {}'.format(aluno, media))
    print('O aluno {} foi reprovado, precisa estudar mais!'.format(aluno))
