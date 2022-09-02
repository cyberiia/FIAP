#!/bin/bash

# Shell Script!
# Laço de repetição WHILE
# Utilizado enquanto uma condição for verdadeira.

read -p "Contagem regressiva: " COUNT

while [ $COUNT -ge 0 ]; do
        echo $COUNT
        let COUNT--
done
