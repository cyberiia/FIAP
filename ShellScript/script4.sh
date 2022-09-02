#!/bin/bash

# Shell Script!
# Condicionais IF...ELSE
# Input diretamente no prompt!

MAIORIDADE=18
TRUE="sim"
FALSE="nao"

read -p "Digite sua idade: " IDADE
read -p "Possui CNH? " CNH

if [ $IDADE -ge $MAIORIDADE ] && [ $CNH == $TRUE ]; then
        echo "Pode dirigir"
else
        echo "Não pode dirigir"
fi

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

echo
read -p "Enter your pet type: " PET

if [ $PET = dog ]; then
        echo "You have a dog!"
fi
