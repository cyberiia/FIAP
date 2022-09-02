# Print, Input, Variáveis e Operadores Aritméticos!

print("\tHello World!")                    # \t é a formatação utilizada para centralizar o texto.
print("\tLet's get started!\n")            # \n é a formatação utilizada para quebra de linhas.

try:
    age = int(input("\tDigite sua idade: ")) # variável com input do tipo int (inteiro), solicitando a idade do usuário.
    if age < 18:                             # condição, se a idade inputada pelo usuário for menor que 18:
        print("\tVocê é menor de idade!")
        quit()
    else:
        print("\tVocê é maior de idade!")
        pass
except:                                    # tratamento de erros, fará o programa se encerrar ao invés de enviar uma mensagem de erro.
    quit()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''
Comentário multilines!

Aprovação ou Reprovação!!
'''

print("\n\tResultado do Exame!")

try:
    nota = int(input("\tSua nota: "))
    if nota in range(6,11): #if nota >= 6 and nota <= 10    # condição com operadores aritméticos
        resultado = "aprovado!"
    elif nota in range(0,6):  #if nota <= 5 and nota >= 0
        resultado = "reprovado!"

    print(f"\n\tSua nota é {nota}, você está {resultado}")  # formatação para exibir os valores das variáveis.

except:
    print("\n\tInsira um número válido!")                   # tratamento de erros.
    quit()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Tipos de input:

int(input(''))    # números inteiros
float(input(''))  # números decimais
str(input(''))    # strings

# Operadores aritméticos/comparativos:

'>'  # maior
'>=' # maior ou igual
'<'  # menor
'<=' # menor ou igual
'==' # igual
'!=' # diferente