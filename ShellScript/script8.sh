#!/bin/bash

# Shell Script!
# Laço de repetição UNTIL
# Utilizado enquanto uma condição for falsa, o loop só para quando retornar verdadeiro.

read -p "Contar até: " COUNT
START=0

until [ $START -gt $COUNT ]; do
        echo $START
        let START++
done
