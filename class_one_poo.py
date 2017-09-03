"""
Author: Henrique Nascimento
Email: nascimentocostahenrique@gmail.com
Facebook Profile: https://www.facebook.com/henrique.nascimento.7568596
"""

class Meu_Objeto:
	def __init__(self, nome, idade):
		self.nome = str(nome)
		self.idade = idade
		print('Chamando o construtor')

	def imprime(nome, idade):
		print('Ola meu nome e ',nome,' e eu tenho %d anos' % (idade))

attr = Meu_Objeto('Henrique', 15)

attr.imprime(idade=15)