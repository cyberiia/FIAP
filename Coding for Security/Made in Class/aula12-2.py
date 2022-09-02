# Manipulação de Arquivos!
# Removendo arquivos e diretórios do sistema utilizando Python!

import os                # Lib do Sistema Operacional
os.remove("newfile.txt") # Exclui apenas arquivos

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Listagem de diretórios filhos

import os
ls = os.listdir("/") # Lista todos os diretórios dentro da partição raíz
print(ls)            # Exibe a listagem na tela

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Deletar um arquivo pelo nome

import os
myfile = input("Arquivo: ")

try:
    os.remove(myfile)                                    # Tenta remover o arquivo inputado
except OSError as e:                                     # Tratamento de erros de I/O
    print ("Error: %s - %s." % (e.filename, e.strerror)) # Exibindo o erro na tela

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Remover um diretório recursivamente

import os
import shutil
mydir = input("Diretório: ")

try:
    shutil.rmtree(mydir)                                 # Tenta remover o diretório
except OSError as e:                                     # Tratamento de erros de I/O
    print ("Error: %s - %s." % (e.filename, e.strerror)) # Exibindo o erro na tela