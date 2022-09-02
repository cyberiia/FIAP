# Ordenação!

frutas = ["Banana","abacaxi","goiaba","Cereja","melancia"]
frutas.sort(key=str.lower, reverse = False)                # Desativando o Case Sensitive (key=str.lower), as palavras são ordenadas corretamente 
print(frutas,'\n')                                         # Reverse ordena de trás para frente

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Função simples para ordenar

def ordem(p):
    return p.lower()

L = ['gama', 'alfa', 'Delta', 'epsilon', 'Beta', 'Zeta']
L.sort(key=ordem, reverse = False)
print(L)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Definir função para ordenar

names = ["Anna", "Judy", "Maya", "Eve", "Mari"]

def ordenar_lista(names):
	len_lista = len(names)  # obtém o tamanho da lista
	for i in range(len_lista - 1, 0, -1):
		for j in range(i):
            # IF testa se a string acessada pelo índice (j + 1)
			if(names[j].lower() > names[j + 1].lower()):   # lower() todos os caracteres para minúsculo
				aux = names[j]                             # precede a string acessada pelo índice "j"
				names[j] = names[j + 1]                    # faz a troca dos elementos
				names[j + 1] = aux

ordenar_lista(names)
print(names,'\n')