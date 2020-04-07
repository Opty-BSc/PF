"""					      	
								PROJETO 2 DE FP               	
									REALIZADO POR:           		
										90774 - Ricardo Grade		
""" 
from parte1 import e_palavra
from itertools import permutations
from string import ascii_uppercase

# TAD palavra_potencial

def cria_palavra_potencial(cad_caracteres, tuplo_letras):
	"""
		:Descricao cria_palavra_potencial: Dada uma cadeia de caracteres e um tuplo de letras \
		constroi a palavra potencial associada
	
	:param cad_caracteres: String que representa a palavra
	:param tuplo_letras: Tuplo que contem as letras que podem ser utilizadas na palavra
	:return: palavra potencial
	Tuplo (String que representa a palavra, Tamanho da string, Tuplo de letras)
	"""
	if not isinstance(cad_caracteres, str) or not isinstance(tuplo_letras, tuple) or \
	not verify_upper(cad_caracteres) or not verify_upper(tuplo_letras):
		raise ValueError ('cria_palavra_potencial:argumentos invalidos.')
 	
	if len(cad_caracteres) > len(tuplo_letras) or not cad_formed_by_tup(cad_caracteres, tuplo_letras):
		raise ValueError ('cria_palavra_potencial:a palavra nao e valida.')

	return (cad_caracteres, len(cad_caracteres), tuplo_letras)


def palavra_tamanho(palavra_potencial):
 	"""
 		:Descricao palavra_tamanho: Dada uma palavra potencial devolve o tamanho da string que representa a palavra
 	
 	:param palavra_potencial: Tuplo que representa a palavra
 	:return: Inteiro
 	"""
 	return palavra_potencial[1]


def e_palavra_potencial(universal):
	"""
		:Descricao e_palavra_potencial: Dado um input devolve o booleano associado a validade do input \  
		aquando comparado a estrutura definida para a palavra potencial
	
	:param universal: Qualquer input
	:return: Booleano
	"""
	return 	isinstance(universal, tuple) and len(universal) == 3 and \
			isinstance(universal[0], str) and verify_upper(universal[0]) and \
			isinstance(universal[1], int) and len(universal[0]) == universal[1] and \
			isinstance(universal[2], tuple) and verify_upper(universal[2]) and \
			cad_formed_by_tup(universal[0], universal[2])


def palavras_potenciais_iguais(palavra_potencial_1, palavra_potencial_2):
	"""
		:Descricao palavras_potenciais_iguais: Dadas 2 palavras potenciais devolve um booleano associado a igualdade \
		das strings que representam as palavras
	
	:param palavra_potencial_1: Tuplo que representa uma palavra potencial
	:param palavra_potencial_2: Tuplo que representa a outra palavra potencial
	:return: Booleano
	"""
	return palavra_potencial_para_cadeia(palavra_potencial_1) == palavra_potencial_para_cadeia(palavra_potencial_2)


def palavra_potencial_menor(palavra_potencial_1, palavra_potencial_2):
	"""
		:Descricao palavra_potencial_menor: Dadas 2 palavras potenciais devolve um booleano 
		- True se a palavra_potencial_1 for alfabeticamente menor que palavra_potencial_2
		- False em caso contrario
	
	:param palavra_potencial_1: Tuplo que representa uma palavra potencial
	:param palavra_potencial_2: Tuplo que representa a outra palavra potencial
	:return: Booleano
	"""
	return palavra_potencial_para_cadeia(palavra_potencial_1) < palavra_potencial_para_cadeia(palavra_potencial_2)


def palavra_potencial_para_cadeia(palavra_potencial):
	"""
		:Descricao palavra_potencial_para_cadeia: Dada uma palavra potencial devolve a sua string associada
	
	:param palavra_potencial: Tuplo que representa a palavra potencial
	:return: String que representa a palavra
	"""
	return palavra_potencial[0]

# TAD conjunto_palavras

def cria_conjunto_palavras():
	"""
		:Descricao cria_conjunto_palavras: Devolve um conjunto de palavras
	
	:return: Lista vazia
	"""
	return []


def numero_palavras(conjunto_palavras):
	"""
		:Descricao numero_palavras: Dado um conjunto de palavras devolve o seu tamanho
	
	:param conjunto_palavras: Lista associada ao conjunto de palavras
	:return: Inteiro
	"""
	return len(conjunto_palavras)


def subconjunto_por_tamanho(conjunto_palavras, n):
	"""
		:Descricao subconjunto_por_tamanho: Dado um conjunto de palavras e um inteiro devolve um conjunto \
		de palavras que contem apenas as palavras do tamanho introduzido
	
	:param conjunto_palavras: Lista associada ao conjunto de palavras
	:param n: Inteiro
	:return: Lista do tipo conjunto de palavras de tamanho n
	"""
	sub_size = cria_conjunto_palavras()
	for pal_pot in conjunto_palavras:
		if palavra_tamanho(pal_pot) == n:
			sub_size.append(pal_pot)

	return sub_size


def acrescenta_palavra(conjunto_palavras, palavra_potencial):
	"""
		:Descricao acrescenta_palavra: Dado um conjunto de palavras e uma palavra potencial acrescenta-a ao conjunto \
		de palavras se e so se a palavra potencial ainda nao estiver no conjunto
	
	:param conjunto_palavras: Lista associada ao conjunto de palavras
	:param palavra_potencial: Tuplo que representa a palavra potencial
	"""
	if not e_palavra_potencial(palavra_potencial) or not e_conjunto_palavras(conjunto_palavras):
		raise ValueError ('acrescenta_palavra:argumentos invalidos.')

	for pal_pot in conjunto_palavras:
		if palavras_potenciais_iguais(palavra_potencial, pal_pot): return

	conjunto_palavras.append(palavra_potencial)
	return


def e_conjunto_palavras(universal):
	"""
		:Descricao e_conjunto_palavras: Dado um input devolve o booleano associado a validade do input \  
		aquando comparado a estrutura de um conjunto de palavras
	
	:param universal: Qualquer input
	:return: Booleano
	"""
	if not isinstance(universal, list): return False

	verify_repet = cria_conjunto_palavras()
	for pal_pot in universal:
		if not e_palavra_potencial(pal_pot): return False

		if pal_pot not in verify_repet:
			verify_repet.append(pal_pot)

	if verify_repet != universal: return False

	return True


def conjuntos_palavras_iguais(conjunto_palavras_1, conjunto_palavras_2):
	"""
		:Descricao conjuntos_palavras_iguais: Dados 2 conjuntos de palavras devolve um booleano associado a igualdade \
		de todos os elementos dos conjuntos de palavras

	:param conjunto_palavras_1: Lista associada a um conjunto de palavras
	:param conjunto_palavras_2: Lista associada a outro conjunto de palavras
	:return: Booleano
	"""
	if numero_palavras(conjunto_palavras_1) == 0 and numero_palavras(conjunto_palavras_2) == 0: return True

	if numero_palavras(conjunto_palavras_1) == 0 or numero_palavras(conjunto_palavras_2) == 0: return False

	for ind in range(numero_palavras(conjunto_palavras_2)):

		if palavras_potenciais_iguais(conjunto_palavras_1[0], conjunto_palavras_2[ind]):

			return conjuntos_palavras_iguais(conjunto_palavras_1[1:], conjunto_palavras_2[:ind] + \
			conjunto_palavras_2[ind+1:])

	return False


def conjunto_palavras_para_cadeia(conjunto_palavras):
 	"""
 		:Descricao conjunto_palavras_para_cadeia: Dado um conjunto de palavras devolve uma String associada que \
 		se encontra ordenada relativamente ao seu tamanho e a sua ordem alfabetica

 	:param conjunto_palavras: Lista associada ao conjunto de palavras
 	:return: String 
 	'Tamanho->[Subconjunto de palavras desse tamanho]' \
 	para todos os tamanhos de palavras existentes no conjunto de palavras
 	"""
 	sizes = cria_conjunto_palavras()
 	for pal_pot in conjunto_palavras:
 		if palavra_tamanho(pal_pot) not in sizes:
 			sizes.append(palavra_tamanho(pal_pot))

 	sizes.sort()
 	word_sizes = cria_conjunto_palavras()
 	for tam in sizes:
 		
 		cadeia_same_size = [palavra_potencial_para_cadeia(pal_pot) for pal_pot in \
 		subconjunto_por_tamanho(conjunto_palavras, tam)]

 		cadeia_same_size.sort()
 		word_sizes.append(cadeia_same_size)

 	pretty_print = ''
 	for ind in range(len(sizes)):
 		pretty_print += '{}->{};'.format(sizes[ind], word_sizes[ind]).replace("'","")

 	return '[' + pretty_print[:-1] + ']'

# 	TAD jogador

def cria_jogador(cad_caracteres):
	"""
		:Descricao cria_jogador: Constroi um jogador dado uma cadeia de caracteres associada ao seu nome

	:param cad_caracteres: String
	:return: Jogador
	Jogador = Lista [String associada ao seu nome, Inteiro associada a Pontuacao, \
	Lista de palavras validas, Lista de palavras invalidas)]
	"""
	if not isinstance(cad_caracteres, str):
		raise ValueError ('cria_jogador:argumento invalido.')

	return [cad_caracteres, 0, cria_conjunto_palavras(), cria_conjunto_palavras()]

	
def jogador_nome(jogador):
	"""
		:Descricao jogador_nome: Dado um jogador devolve o seu nome

	:param jogador: Lista associada ao jogador
	:return: String
	"""
	return jogador[0]


def jogador_pontuacao(jogador):
	"""
	 	:Descricao jogador_pontuacao: Dado um jogador devolve a sua pontuacao

	:param jogador: Lista associada ao jogador
	:return: Inteiro
	"""
	return jogador[1]
			

def jogador_palavras_validas(jogador):
	"""
	 	:Descricao jogador_palavras_validas: Dado um jogador devolve o conjunto \
	 	de palavras associado as palavras validas introduzidas pelo jogador

	:param jogador: Lista associada ao jogador
	:return: Lista do tipo conjunto de palavras
	"""
	return jogador[2]


def jogador_palavras_invalidas(jogador):
	"""
	 	:Descricao jogador_palavras_invalidas: Dado um jogador devolve o conjunto \
	 	de palavras associado as palavras invalidas introduzidas pelo jogador

	:param jogador: Lista associada ao jogador
	:return: Lista do tipo conjunto de palavras
	"""
	return jogador[3]


def adiciona_palavra_valida(jogador, p):
	"""
		:Descricao adiciona_palavra_valida: Dado um jogador acrescenta a palavra potencial \
		ao conjunto de palavras associado as palavras validas do jogador se e so se esta \
		ainda nao lhe estiver associada  
	
	:param jogador: Lista associada ao jogador
	:param p: Tuplo que representa a palavra potencial
	"""
	if not e_jogador(jogador) or not e_palavra_potencial(p):
		raise ValueError ('adiciona_palavra_valida:argumentos invalidos.')

	for pal_val in jogador_palavras_validas(jogador):
		if palavras_potenciais_iguais(p, pal_val): return

	jogador[1] = jogador_pontuacao(jogador) + palavra_tamanho(p)
	acrescenta_palavra(jogador_palavras_validas(jogador), p)
	return


def adiciona_palavra_invalida(jogador, p):
	"""
		:Descricao adiciona_palavra_invalida: Dado um jogador acrescenta a palavra potencial \
		ao conjunto de palavras associado as palavras invalidas do jogador se e so se esta \
		ainda nao lhe estiver associada  
	
	:param jogador: Lista associada ao jogador
	:param p: Tuplo que representa a palavra potencial
	"""
	if not e_jogador(jogador) or not e_palavra_potencial(p):
		raise ValueError ('adiciona_palavra_invalida:argumentos invalidos.')

	for pal_inval in jogador_palavras_invalidas(jogador):
		if palavras_potenciais_iguais(p, pal_inval): return

	jogador[1] = jogador_pontuacao(jogador) - palavra_tamanho(p)
	acrescenta_palavra(jogador_palavras_invalidas(jogador), p)
	return


def e_jogador(universal):
	"""
		:Descricao e_jogador: Dado um input devolve o booleano associado a validade do input \  
		aquando comparado a estrutura de um jogador
	
	:param universal: Qualquer input
	:return: Booleano
	"""
	return 	isinstance(universal, list) and len(universal) == 4 and \
			isinstance(jogador_nome(universal), str) and \
			isinstance(jogador_pontuacao(universal), int) and \
			e_conjunto_palavras(jogador_palavras_validas(universal)) and \
			e_conjunto_palavras(jogador_palavras_invalidas(universal))


def jogador_para_cadeia(jogador):
	"""
 		:Descricao conjunto_palavras_para_cadeia: Dado um jogador devolve uma String associada que \
 		contem o seu nome, a sua pontuacao, e as cadeias associadas aos conjuntos de palavras das \
 		palavras validas e invalidas introduzidas pelo jogador

 	:param jogador: Lista associada ao jogador
 	:return: String as estatisticas do jogador
 	'JOGADOR nome PONTOS=pontuacao VALIDAS=palavras validas INVALIDAS=palavras invalidas'
 	"""

	return 'JOGADOR {} PONTOS={} VALIDAS={} INVALIDAS={}'.format(jogador_nome(jogador), \
			jogador_pontuacao(jogador), conjunto_palavras_para_cadeia(jogador_palavras_validas(jogador)), \
			conjunto_palavras_para_cadeia(jogador_palavras_invalidas(jogador)))

# Funcoes Adicionais

def gera_todas_palavras_validas(tuplo_letras):
	"""
		:Descricao gera_todas_palavras_validas: Dado um tuplo de letras gera todas as palavras validas \
		associadas a Gramatica Guru, que e possivel formar usando exclusivamente as letras do tuplo

	:param tuplo_letras: Tuplo que contem as letras que podem ser utilizadas na palavra
	:return: Conjunto de palavras validas
	"""
	list_permutations = cria_conjunto_palavras()

	for tam in range(1, len(tuplo_letras)+1):
		for tuplo in permutations(tuplo_letras, tam):
			str_permutation = ''
			for letter in tuplo:
				str_permutation += letter
			if e_palavra(str_permutation):
				acrescenta_palavra(list_permutations, cria_palavra_potencial(str_permutation, tuplo_letras))

	return list_permutations


def guru_mj(tuplo_letras):
	"""
	 	:Descricao guru_mj: Esta funcao permite desenrolar o jogo Multi Jogador Palavras Guru
	
	:param tuplo_letras: Tuplo de letras a usar no jogo
	"""
	def sel_jogador(n=1, list_jogadores=cria_conjunto_palavras()):
		"""
			 :Descricao sel_jogador: E uma funcao complementar da guru_mj que tem como funcao inscrever os jogadores

		:return: Lista que contem todos os jogadores
		"""
		input_jogador = input('JOGADOR {} -> '.format(n))

		if input_jogador == '-1':
			return list_jogadores

		list_jogadores.append(cria_jogador(input_jogador))
		
		return sel_jogador(n+1)


	def main_guru(tuplo_letras, palavras_validas, list_jogadores, palavras_validas_left, n=1, i=0):
		"""
			:Descricao main_guru: E uma funcao complementar da guru_mj onde se desenrola o jogo propriamente dito

		:param tuplo_letras: Tuplo que contem as letras que podem ser utilizadas na palavra
		:param palavras_validas: Conjunto de palavras validas
		:param list_jogadores: Lista que contem todos os jogadores
		:param palavras_validas_left: Copia das palavras_validas, utilizada para saber se a palavra ja foi introduzida
		"""
		if numero_palavras(palavras_validas_left) == 0: return

		print('JOGADA {} - Falta descobrir {} palavras'.format(n, numero_palavras(palavras_validas_left)))

		if i == len(list_jogadores):
			i = 0
		jogador = list_jogadores[i]

		input_jogada = input('JOGADOR {} -> '.format(jogador_nome(jogador)))
		palavra_potencial = cria_palavra_potencial(input_jogada, tuplo_letras)

		if palavra_potencial in palavras_validas:
			print('{} - palavra VALIDA'.format(input_jogada))
			if palavra_potencial in palavras_validas_left:
				adiciona_palavra_valida(jogador, palavra_potencial)
				palavras_validas_left.remove(palavra_potencial)

		else:
			print('{} - palavra INVALIDA'.format(input_jogada))
			adiciona_palavra_invalida(jogador, palavra_potencial)

		return main_guru(tuplo_letras, palavras_validas, list_jogadores, palavras_validas_left, n+1, i+1)


	def termina_jogo(list_jogadores, list_pontuacao=cria_conjunto_palavras()):
		"""
			:Descricao termina_jogo: E uma funcao complementar da guru_mj que designa o vencedor, ou caso nao haja o empate

		:param list_jogadores: Lista que contem todos os jogadores
		"""
		for jog in list_jogadores:
			list_pontuacao.append(jogador_pontuacao(jog))

		list_pontuacao.sort()

		def empate(list_pontuacao):

			for pont in list_pontuacao[:-1]:
				if pont == list_pontuacao[-1]: return True

			return False

		if not empate(list_pontuacao):
			for jog in list_jogadores:
				if jogador_pontuacao(jog) == list_pontuacao[-1]:
					vencedor = jogador_nome(jog)
					pontuacao_vencedor = list_pontuacao[-1]
					break

			print('FIM DE JOGO! O jogo terminou com a vitoria do jogador', end=' ')
			print('{} com {} pontos.'.format(vencedor, pontuacao_vencedor))

		else:
			print('FIM DE JOGO! O jogo terminou em empate.')

		return


	print('Descubra todas as palavras geradas a partir das letras:\n{}'.format(tuplo_letras))
	print('Introduza o nome dos jogadores (-1 para terminar)...')

	list_jogadores = sel_jogador()
	palavras_validas = gera_todas_palavras_validas(tuplo_letras)

	main_guru(tuplo_letras, list(palavras_validas), list_jogadores, list(palavras_validas))
	termina_jogo(list_jogadores)

	for jog in list_jogadores:
		print(jogador_para_cadeia(jog))

	return

# Funcoes Auxiliares

def verify_upper(universal):
	"""
		:Descricao verify_upper: Dado um input devolve um booleano associado a se tem apenas letras maiusculas
	
	:param verify_upper: Qualquer input
	:return: Booleano
	"""
	for car in universal:
		if str(car) not in ascii_uppercase or len(str(car)) > 1: return False

	return True


def cad_formed_by_tup(cad_caracteres, tuplo_letras):
	"""
		:Descricao cad_formed_by_tup: Dado uma string e um tuplo de letras devolve um booleano de acordo \
		com a possibilidade da string se escrever exclusivamente com as letras do tuplo

	:param cad_caracteres: String
	:param tuplo_letras: Tuplo que contem as letras que podem ser utilizadas na string
	:return: Booleano
	"""
	verify_list = list(tuplo_letras)
	for letter in cad_caracteres:
		if letter not in verify_list: return False
		verify_list.remove(letter)

	return True