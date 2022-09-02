#!/bin/bash

# Shell Script!
# Condicionais IF...ELSE
# Passando input como parâmetro!

MAIORIDADE=18

if [ $1 -ge $MAIORIDADE ]; then
        echo "Maior de idade."
else
        echo "Menor de idade."
fi
