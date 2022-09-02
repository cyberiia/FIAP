#!/bin/bash

# Shell Script!
# Dicionários em Bash!

declare -A things

things=(["fruit"]="banana" ["animal"]="dog" ["color"]="yellow")

for i in "${!things[@]}"; do
        echo "$i"="${things[$i]}"
done
