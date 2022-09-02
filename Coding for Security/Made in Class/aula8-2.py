# Ordenação com For!

print("Ordenar palavras ou números!")
escolha = input("\na) Ordem crescente\nb) Ordem decrescente\n➔ ")
options = ["a","b"]

if escolha not in options:
    quit()
    
a = input('\nInsira os elementos ➔ ').split(' ')   # .split() identifica que cada palavra é independente de cada 'espaço'
if len(a) < 2:                                     # len é a quantidade de palavras do input
    print("\n⚠ Insira mais de um elemento!")
    quit()

print("\n--------------------------------\n")
# Ordem crescente

if escolha == "a":
    for i in range(len(a)):
        for j in range (len(a)):
            if a[j] > a[i]: # Essa função irá ordenar
                swth = a[i] # Variável temporária para fazer a mudança
                a[i] = a[j]
                a[j] = swth

    print('Ordem crescente:\n ')
    for item in a:
        print('•', item, end='\n')

#~~~~~~~~~~~~~~~~~~~~~~~~~
# Ordem decrescente

if escolha == "b":
    for i in range(len(a)):
        for j in range(len(a)):
            if a[j] < a[i]: # Essa função irá ordenar
                swth = a[i] # Variável temporária para fazer a mudança
                a[i] = a[j]
                a[j] = swth

    print('Ordem decrescente:\n ')
    for item in a: 
        print('•', item, end='\n')