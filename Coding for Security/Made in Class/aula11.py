# Definindo funções!
# Funções são utilizadas para reduzir o código, podemos chamá-las várias vezes!

def hello(nome, idade):                          # Nome e idade são argumentos da função
    print(f"Olá {nome}, você tem {idade} anos!") # Resultado da função

nome = input('Nome: ')                           # Primeiro argumento da função
idade = int(input('Idade: '))                    # Segundo argumento da função
hello(nome,idade)
print()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Função para contagem de números

def print_num(n):
    if n > 0:
        print_num(n - 1)
    print(n,'\n', end = '')
print_num(130)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Função para cálculos

def soma(numA, numB):
    print("Resultado:", numA + numB)

numA = int(input('Número: '))
numB = int(input('Número: '))
soma(numA,numB)
print()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Função para calcular salário

def pagamento(horas, valor):
    salario=float(horas)*float(valor)*5.5
    return salario

horas_t= input("Digite as horas: ")
valor_h=input("Digite o valor hora: ")
print(f"O salário é R${pagamento(horas_t,valor_h)}")
print()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Função para calcular o fatorial

def fatorial(n):
    if n <= 1:
        return 1
    else:
        return n * fatorial(n-1) #recursivo
        
print("Cálculo do Fatorial de N")
x = int(input("Digite o valor de n: "))
f = fatorial(x)
print("O fatorial de {0} é {1}".format(x,f))