
"""					      	

								PROJETO 1 DE FP               	
									REALIZADO POR:           		
										90774 - Ricardo Grade		
						
"""
def tuple_distributive(tuple_1,tuple_2):
	len_tuple_1 = len(tuple_1)							# 	Nr de elementos do tuple_1
	len_tuple_2 = len(tuple_2)							# 	Nr de elementos do tuple_2
	tuple_3 = tuple_1 									# 	tuple_3 serve para dar "reset" ao tuple_1
	tuple_4 = () 
	for t in range (len_tuple_2):						# 	Para todas as strings da ordem do tuple_2
		for i in range (len_tuple_1): 					# 	Para todas as strings da ordem do tuple_1
			str_conc = tuple_1[i] + tuple_2[t]			# 	Concatena numa string as de ordem i e t dos dois tuplos
			tuple_1 = tuple_1[:i] + (str_conc,) + tuple_1[i + 1:]
		#	tuple_1 e um tuplo cujos elementos sao as strings do tuple_1 concatenadas com a string do tuple_2 de ordem t
		tuple_4 += tuple_1 								# 	tuple_4 e o tuple concatenado de todas as tuple_1's
		tuple_1 = tuple_3 								# 	tuple_1 "reseta"
	return tuple_4
"""

	A Funcao tuple_distributive funciona como a propriedade distributiva
	Cada string do tuple_1 concatena (separadamente) com todas as strings do tuple_2, por exemplo:
		tuple_1 = ('A','B')
		tuple_2 = ('C','D')
		tuple_distributive(tuple_1,tuple_2) retorna o tuplo ('AC','AD','BC','BD')

"""
"""						
					
							GRAMATICA GURU 			
							
"""
artigo_def = ('A','O')
vogal_palavra = artigo_def + ('E',)
vogal = ('I','U') + vogal_palavra
ditongo_palavra = ('AI','AO','EU','OU')
ditongo = ('AE','AU','EI','OE','OI','IU') + ditongo_palavra
par_vogais = ditongo + ('IA','IO')
consoante_freq = ('D','L','M','N','P','R','S','T','V')
consoante_terminal = ('L','M','R','S','X','Z')
consoante_final = ('N','P') + consoante_terminal
consoante = ('B','C','D','F','G','H','J','L','M','N','P','Q','R','S','T','V','X','Z')
par_consoantes = ('BR','CR','FR','GR','PR','TR','VR','BL','CL','FL','GL','PL')
monossilabo_2 = ('AR','IR','EM','UM') + tuple_distributive(vogal_palavra,('S',)) + ditongo_palavra + tuple_distributive(consoante_freq,vogal)
monossilabo_3_incomplete = tuple_distributive(tuple_distributive(consoante,vogal),consoante_terminal) + tuple_distributive(consoante,ditongo)
monossilabo_3 = monossilabo_3_incomplete + tuple_distributive(par_vogais,consoante_terminal)
monossilabo = vogal_palavra + monossilabo_2 + monossilabo_3
silaba_2 = par_vogais + tuple_distributive(consoante,vogal) + tuple_distributive(vogal,consoante_final)
silaba_3_incomplete_1 = ('QUA','QUE','QUI','GUE','GUI') + tuple_distributive(vogal,('NS',)) + tuple_distributive(consoante,par_vogais)
silaba_3_incomplete_2 = silaba_3_incomplete_1 + tuple_distributive(tuple_distributive(consoante,vogal),consoante_final) 
silaba_3 = silaba_3_incomplete_2 + tuple_distributive(par_vogais,consoante_final) + tuple_distributive(par_consoantes,vogal)
silaba_4_incomplete_1 = tuple_distributive(par_vogais,('NS',)) + tuple_distributive(tuple_distributive(consoante,vogal),('NS',))
silaba_4_incomplete_2 = silaba_4_incomplete_1 + tuple_distributive(tuple_distributive(consoante,vogal),('IS',))
silaba_4 = silaba_4_incomplete_2 + tuple_distributive(par_consoantes,par_vogais) + tuple_distributive(tuple_distributive(consoante,par_vogais),consoante_final)
silaba_5 = tuple_distributive(tuple_distributive(par_consoantes,vogal),('NS',))
silaba_final = monossilabo_2 + monossilabo_3 + silaba_4 + silaba_5
silaba = vogal + silaba_2 + silaba_3 + silaba_4 + silaba_5
letras_validas = ('A','B','C','D','E','F','G','H','I','J','L','M','N','O','P','Q','R','S','T','U','V','X','Z')

def e_silaba(cad_caracteres):
	if type(cad_caracteres) != str:     	
		raise ValueError ('e_silaba:argumento invalido')
	for i in cad_caracteres: 					# 	Para todas os caracteres da cad_caracteres
		if i not in letras_validas: 			# 	Se houver algum que nao seja uma letra que pertenca a Gramatica
			return False
	if cad_caracteres in silaba:				#	Verifica se a cad_caracteres e uma silaba valida
		return True
	else: 
		return False 
"""	

	A Funcao e_silaba verifica a validade da silaba introduzida

"""
def e_monossilabo(cad_caracteres):
	if type(cad_caracteres) != str:  					
		raise ValueError ('e_monossilabo:argumento invalido') 
	for i in cad_caracteres: 					# 	Para todas os caracteres da cad_caracteres
		if i not in letras_validas: 			# 	Se houver algum que nao seja uma letra que pertenca a Gramatica
			return False
	if cad_caracteres in monossilabo: 			#	Verifica se a cad_caracteres e um monossilabo valido
		return True
	else: 
		return False
"""

	A Funcao e_monossilabo verifica a validade do monossilabo introduzido

"""
def sil_verify(cad_caracteres):
	list_sil = []
	i = 1
	while i <= 5:
		if cad_caracteres[:i] in silaba:	# 	Para cada valor de i int [1,5] testa uma silaba com os caracteres respetivos
			list_sil += [i]					# 	Guarda os valores de i na list_sil para os quais a condicao se verifica
		i += 1
	for i in list_sil: 						# 	Para todos os valores da list_sil
		if cad_caracteres[:i] == cad_caracteres:
		# 	Quando a cad_caracteres for igual a uma das silabas possiveis a funcao termina (quando a palavra e True)
			return True
		if sil_verify(cad_caracteres[i:]):
		# 	Quando a condicao de cima se verifica todas as outras que a chamaram retornam True
			return True
		# 	Senao quando acabar de testar todas as sequencias de silabas possiveis a funcao termina (quando a palavra e False)
	return False
"""

	A Funcao sil_verify chama-se a si propria, fazendo uma recursiva, que testa todas as possibilidades de
	se formarem silabas com os caracteres da palavra(ja excluindo os da silaba_final, que foram retirados na funcao sil_sil_final_verify)

"""
def sil_sil_final_verify(cad_caracteres):
	list_sil_final = []
	i = 1
	while i <= 5:
		if cad_caracteres[-i:] in silaba_final: 	#	Para cada valor de i int [1,5] testa uma silaba_final com os caracteres respetivo
			list_sil_final += [-i] 					#	Adiciona a list_sil_final a ordem a partir da qual comeca uma silaba_final valida
		i += 1
	for i in list_sil_final: 						# 	Para todos os valores da list_sil_final
		if sil_verify(cad_caracteres[:i]): 			# 	Se os caracteres que vierem atras dessa silaba formarem uma cadeia de silabas validas
			return True
	# 	Se nenhuma sequencia for valida
	return False
"""

	A Funcao sil_sil_final_verify chama a funcao sil_verify para todas as iniciais duma silaba_final da palavra,
	tirando-a da mesma para verificar a validade duma possivel cadeia de silabas sequenciais 

"""
def e_palavra(cad_caracteres):
	if type(cad_caracteres) != str:
		raise ValueError ('e_palavra:argumento invalido')
	for i in cad_caracteres: 					# 	Para todas os caracteres da cad_caracteres
		if i not in letras_validas: 			# 	Se houver algum que nao seja uma letra que pertenca a Gramatica
			return False
	if cad_caracteres in monossilabo: 			#	Verifica se a cad_caracteres e um monossilabo valido
		return True
	elif cad_caracteres in silaba_final: 		# 	Se nao verifica se a cad_caracteres e uma silaba_final valida
		return True
	elif sil_sil_final_verify(cad_caracteres):	# 	Se nao verifica se a cad_caracteres e formada por uma cadeia de silabas, seguida de uma silaba_final
		return True
	else:
		return False
"""

	A Funcao e_palavra verifica a validade da palavra introduzida, verificando se e monossilabo, silaba final,
	ou uma sequencia de silabas terminadas com uma silaba_final

"""