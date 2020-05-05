class Pessoa(object):


    def __init__(self, n, i, a, p):
        self.nome = n
        self.idade = i
        self.altura = a
        self.peso = p

    def mostra(self):
        print(f'{self.nome} tem {self.idade} anos\nMede {self.altura} m \nPesa {self.peso} Kg.')

    def imc(self):
        print(f'O IMC de Pablo é: {self.peso / (self.altura * self.altura):5.2f}'.center(50))
