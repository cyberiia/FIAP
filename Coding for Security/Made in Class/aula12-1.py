# Manipulação de Arquivos!
# Abrindo, lendo e escrevendo em arquivos utilizando Python!

file = open('testfile.txt', 'r', encoding='utf-8') # Abrindo arquivo em modo leitura + encoding UTF-8 para formatar o texto
content = file.read()                             # Lê o conteúdo do arquivo
print(content)                                    # Exibindo o conteúdo do arquivo na tela
file.close()                                      # Fecha o arquivo

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Ler linhas específicas do arquivo

file = open('testfile.txt', 'r', encoding='utf-8')
firstLine = file.readline()  # Lê a 1ª linha
secondLine = file.readline() # Lê a 2ª linha
thirdLine = file.readline()  # Lê a 3ª linha
print(firstLine)  # Exibe a 1ª linha
print(secondLine) # Exibe a 2ª linha
print(thirdLine)  # Exibe a 3ª linha
file.close()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Gravando dados em um arquivo

file = open('newfile.txt', 'w', encoding='utf-8') # Modo escrita
file.write('Manipulando Arquivos\n')              # Quebra a linha
file.write('com Python!!')                        # Escreve na linha abaixo
file.close()
