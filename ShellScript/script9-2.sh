#!/bin/bash

# Shell Script!
# Tabuada com FOR Statement!

read -p "Tabuada do: " NUM

for i in $(seq 0 10); do
        R=`echo $NUM \* $i | bc`
        echo "$NUM x $i = $R"
done
