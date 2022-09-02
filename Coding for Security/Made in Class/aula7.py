# Laço de Repetição com While Statement!

# While (Enquanto) for verdadeiro (True), as instruções serão executadas, até que haja uma interrupção (keyboard, bufferoverflow, etc).
# Se não houver interrupções e retornar True, o loop será executado constantemente.

print(f"Contagem de Números")
cont = int(input("Início: "))
fim = int(input("Até: "))
while cont < fim:      # Contagem progressiva
    print(cont)        # Exibe o primeiro número da contagem
    cont+=1            # Atualiza a variável adicionando 1
while cont >= fim:     # Contagem regressiva
    print(cont)
    cont-=1
print("Fim da Contagem\n")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Cálculo de Fatorial com Python

print("Cálculo do Fatorial")
núm = int(input("Número: "))
result = 1
count = 1
while count <= núm:
    result *= count  # result = result * count  | new_var = old_var * 1 
    count += 1       # count = count + 1        | new_var = old_var + 1
print(f"Fatorial: {result}\n")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# While só é executado se retornar verdadeiro:

while 1:
    print("Criação de Loops com While!")
    break

while 1>2:                       # Loop que ocorrerá se uma condição for verdadeira
    print("Hello World!")        # Como 1 é menor que 2, as instruções não serão executadas
    pass            # Passar, e executar outras instruções
    continue        # Continuar a execução do código
    break           # Utilizado para quebrar o loop

while True:
    print("É verdadeiro!")
    break

while False:
    print("É falso!")
    break

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# While também pode ser utilizado para tratar erros:

while 1:                                         # Loop criado para manter o programa funcionando

    numA = int(input("Insira um número: "))

    operadores_válidos = ["+","-","*","/","**"]  # Limitando os operadores que o usuário pode inputar
    ação = input("Insira a operação: ")          # Input da operação
    while ação not in operadores_válidos:        # Se a operação inputada não estiver dentro das válidas, o programa se encerrará. O while pode ser substituído pelo If nesse caso.
        print("Insira uma operação válida!")
        quit()
        
    numB = int(input("Insira outro número: "))

    def resultado():
        print(f"{numA} {ação} {numB} = {result}")

    #~~~~~~~~~~~~~~~~~~~~~~~~

    if ação == "+":
        result = numA + numB
        resultado()

    elif ação == "-":
        result = numA - numB
        resultado()

    elif ação == "*":
        result = numA * numB
        resultado()

    elif ação == "/":
        result = numA / numB
        resultado()

    elif ação == "**":
        result = numA ** numB
        resultado()

    # Se não introduzirmos 'break' no final, o loop continuará sendo executado.