"""Elabore um programa para solicitar o nome de uma equipe de futebol,
a quantidade de derrotas, empates e vitórias obtidas por ela no campeonato.
Calcular e informar: a quantidade de pontos ganhos e a quantidade de pontos perdidos."""

nom = str(input('Digite o nome da equipe de futebol: '))
der = int(input('Número de derrotas no campeonato? '))
emp = int(input('Número de empates no campeonato? '))
vit = int(input('Número de vitórias no campeonato? '))
pg = vit * 3 + emp
tp = (der + emp + vit) * 3
pp = tp - pg
print('O campeonato teve um total de {} pontos disputados.\n'
      'O time {} ganhou {} pontos e perdeu {} pontos.'.format(tp, nom, pg, pp))
