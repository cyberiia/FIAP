# Formatação no Python!

print('PYTHON'.lower())  # Transforma maíusculas em minúsculas
print('python'.upper())  # Transforma minúsculas em maíusculas

string = "Programação"
print(string[0:])   # exibe a string do início ao fim
print(string[:-1])  # exibe a string sem o último caractere
print(string[::-1]) # exibe a string de trás para frente
print(string[::3])  # pula os caracteres de 3 em 3

for i in string:
    print(i, end=' ')

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

a = int(input("Insira um número: "))                               # \t é utilizado para dar espaçamento 
b = int(input("Insira outro número: "))

soma = a + b
print(f"\n{a} + {b} = {soma}")                                       # \n é para quebrar a linha
print(f"A soma de {a} com {b} é {soma}")                             # f no início é para formatar, o que está entre chaves será revertido para seu formato original

subtração = a - b
print("\n{0} - {1} = {2}".format(a, b, subtração))                   # .format( variáveis ) irá formatar todas as variáveis dentro dos parênteses para seu formato original
print("A subtração de {0} com {1} é {2}\n".format(a, b, subtração))  # no caso: {0} = a, {1} = b, {2} = subtração

multiplicação = a * b
print(a, "*", b, "=", multiplicação)                                 # neste caso, as variáveis foram colocadas fora da string, e manterão seu formato original
print("A multiplicação de", a, "com", b, "é", multiplicação)

divisão = a / b
print(f"\n{a} / {b} = {divisão:.2f}")                                # :.2f é utilizado para limitar as casas após a vírgula, se resultar em um número decimal
print("A divisão de {0} por {1} é {2:.3f}\n".format(a, b, divisão))


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
# Formatação de Moeda

faturamento = float(input("Faturamento: "))
custo = float(input("Custo: "))
lucro = faturamento - custo
print(f"O lucro foi de R${lucro:,}")       # ":" diz para o python que a variável será formatada, "," é o separador de milhar
print(f"O lucro foi de R${lucro:.2f}")     # ".2" diz para o python que terá duas casas decimais, "f" significa float 
print(f"O lucro foi de R${lucro:,.2f}")    # irá inserir o separador de milhar, juntamente com as casas após a vírgula, é uma exibição mais completa

# Moeda no formato BR:                                      # substituiremos vírgula por ponto e ponto por vírgula, como no fomato da moeda brasileira
texto_lucro = f"R${lucro:_.2f}"                             # substituir vírgula por ponto e depois ponto por vírgula, resultaria em um erro (duas vírgulas), então o underline é utilizado
texto_lucro = texto_lucro.replace(".",",").replace("_",".") # replace é utilizado para trocar todos os itens entre parênteses
print(f"O lucro foi de {texto_lucro}\n")

margem = lucro / faturamento
print(f"A margem foi de {margem:.2f}")
print(f"A margem foi de {margem:.1%}\n")   # substituir "f" de "float" por "%" formatará o resultado em percentual


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

a = int(input("Valor de A: "))
b = int(input("Valor de B: "))
c = a + b

print("\n{0:.2f} + {1:.2f} = {2:.2f}".format(a,b,c))
print(f"{a:.2f} + {b:.2f} = {c:.2f}\n")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

lista = ["banana", "maçã", "uva", "abacaxi"]

for fruta in lista:
    print(f"{fruta}\n", end='')                                      # parâmetro "end" é utilizado para adicionar caracteres ao final de cada elemento

