#!/bin/bash

# Shell Script!
# Listas em Bash!

Linux=('Debian' 'Redhat' 'Ubuntu' 'Android' 'Fedora' 'Suse')
x=3

Linux=(${Linux[@]:0:$x} ${Linux[@]:$(($x + 1))})
echo "${Linux[@]}"
