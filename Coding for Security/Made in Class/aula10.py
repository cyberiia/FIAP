# Utilização do For!
# For é utilizado para criar loops sobre uma sequência

print('Numbers from 1 to 10:')
for n in range(1,11): # Todos os números dentro do range
    print(n, end='')
print('\n')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Cálculo do Fatorial

num = int(input("Fatorial: "))
result = 1

for i in range(1,num+1):
    result*=i # result = result * i
print(result,'\n')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Tabuada

valor = int(input("Tabulada do: "))
for i in range(1,11):
    r = valor * i
    print(f"{valor} * {i} = {r}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Calculadora Simples
# Uso de For e dicionário

numA = int(input("\nInsira o primeiro número: "))
operação = input("Insira a operação: ")
numB = int(input("Insira o segundo número: "))

operaçõesVálidas = {     # Limitando o input
    "+":  [numA+numB],   # Soma
    "-":  [numA-numB],   # Subtração
    "*":  [numA*numB],   # Multiplicação
    "/":  [numA/numB],   # Divisão
    "**": [numA**numB]   # Potenciação
}

for op in operaçõesVálidas[operação]:
    string = str(op)
    print(f"\n{numA} {operação} {numB} = {string}")