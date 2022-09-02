# Introdução a Listas!

lista = ["banana", "maçã", "morango", "abacaxi", "uva", "laranja"]
for item in lista:
    print(f"{item}\n", end='')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Tuplas

db = []                                                          # Lista vazia
user = ('Julieta Neves',   22, '300.429.810-42', 'Minas Gerais') # Variável que armazena mais de um valor
db.append(user)                                                  # .append é utilizado para adicionar os itens na lista
user = ('Fernando Soares', 34, '128.436.880-78', 'São Paulo')
db.append(user)
user = ('Sandra Oliveira', 28, '317.304.630-70', 'Rio de Janeiro')
db.append(user)
user = ('Miguel Carvalho', 19, '401.533.870-76', 'Santa Catarina')
db.append(user)

for (nome, idade, cpf, estado) in db:   # Trata os itens de cada produto na ordem {0},{1},{2},{3}
    print(f"Nome: {nome}")              # {0} de cada usuário
    print(f"Idade: {idade} anos")       # {1} de cada usuário
    print(f"CPF: {cpf}")                # {2} de cada usuário
    print(f"Estado: {estado}")          # {3} de cada usuário
    print()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Minha Fibonacci

a = 1
b = 1
c = a + b
lista = [a,b,c]

while a <= 1000:
    a = b + c       # Atualizará a variável 'a' em um loop
    b = a + c       # Atualizará a variável 'b' em um loop
    c = a + b       # Atualizará a variável 'c' em um loop
    lista.append(a) # Adicionará a variável a lista
    lista.append(b)
    lista.append(c)
print(lista)

#~~~~~~~~~~~~~~~~~~
# Fibonacci Cabrini

n = 0
while n < 2:
    try:
        n = int(input("Digite o valor de n (n > 1): "))
        if n < 2:
            print("Digite n >= 2")
    except:
        print("O número digitado deve ser inteiro!")
lista = [1, 1]
for i in range (n-2):
    lista.append(lista[i] + lista [i+1])
print ("Sequência gerada:", lista)
print("\n\nFim do Programa")