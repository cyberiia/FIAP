#!/bin/bash

# Shell Script!
# Condicional CASE (caso...)

FILE=/root/ShellScripts/Learning/ConditionalCase.txt

#~~~~~~~~~~~~~~~~~
# Conditional Case

case $1 in
        start)
                echo "Iniciando programa"
                sleep 2
                echo "..."
                sleep 2
                echo "......"
                [ -f $FILE ] && echo "Programa iniciado com sucesso!" || > $FILE && echo "O programa foi iniciado com sucesso!"
        ;;
        stop)

                echo "Parando programa"
                sleep 2
                echo "..."
                sleep 2
                echo "......"
                [ -f $FILE ] && rm -rf $FILE && echo "Programa parado com sucesso!" || echo "O programa já está parado!"
        ;;
        status)
                [ -f $FILE ] && echo "O programa está em execução!" || echo "O programa está parado!"
        ;;
        kill)
                [ -f $FILE ] && rm -rf $FILE && kill $$
        ;;
        *)
                echo "Parâmetro desconhecido!"
        ;;
esac
