#!/bin/bash

# Shell Script!
# Laço de repetição FOR
# Utilizado quando existe uma variedade de alvos para satisfazer uma ação.

for DIA in segunda terça quarta quinta sexta; do
        echo $DIA-feira
done

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

COUNT=10

for num in $(seq $COUNT); do
        echo -e $num
done
