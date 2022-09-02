#!/bin/bash

# Shell Script!
# Condicional TEST [] 

MAIORIDADE=18
read -p "Qual é a sua idade? " IDADE

[ $IDADE -ge 18 ] && echo "Você é maior de idade" || echo "Você é menor de idade"
