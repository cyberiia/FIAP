#!/bin/bash

# Shell Script!
# Exibe as variáveis de controle do shell:

echo -e "Variável \$0 armazena o nome do programa: $0"
echo -e "Variável \$1 armazena o primeiro parâmetro após o script: $1"
echo -e "Variável \$2 armazena o segundo parâmetro após o script: $2"
echo -e "Variável \$3 armazena o terceiro parâmetro após o script: $3"
echo -e "Variável \$* ou \$@ armazena todos os parâmetros após o script: $*"
echo -e "Variável \$$ armazena o PID desse script em execução: $$"
echo -e "Variável \$? armazena o código de retorno do último comando executado: $?"
