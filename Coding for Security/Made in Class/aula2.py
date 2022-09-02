# Calculadora Simples!

print('\033[1;31m' + "\n\t/~` _ | _   | _  _| _  _ _ " + '\033[0m') # código para deixar em negrito
print('\033[1;31m' + "\t\_,(_||(_|_||(_|(_|(_)| (_|" + '\033[0m')

ajuda = input("\n\t• Ajuda? (y/N) ")

if ajuda == "y":
    print('\033[31m' + "\n\t ┍━━━━━━━━━━━━━━━━━━━━━━━┑" + '\033[0m')
    print('\033[31m' + "\t |                       |" + '\033[0m')
    print('\033[31m' + "\t |  • Adição (+)         |" + '\033[0m')
    print('\033[31m' + "\t |  • Subtração (-)      |" + '\033[0m')
    print('\033[31m' + "\t |  • Multiplicação (*)  |" + '\033[0m')
    print('\033[31m' + "\t |  • Divisão (/)        |" + '\033[0m')
    print('\033[31m' + "\t |  • Potênciação (**)   |" + '\033[0m')
    print('\033[31m' + "\t |                       |" + '\033[0m')
    print('\033[31m' + "\t ┕━━━━━━━━━━━━━━━━━━━━━━━┙" + '\033[0m')
    pass
else:
    pass

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

while 1:

    try:
        numA = int(input("\n\tInsira o primeiro número: "))
        operação = input("\tInsira a operação: ")
        numB = int(input("\tInsira o segundo número: "))

        operaçõesVálidas = {
            "+":  [numA+numB],
            "-":  [numA-numB],
            "*":  [numA*numB],
            "/":  [numA/numB],
            "**": [numA**numB]
        }
        
        for op in operaçõesVálidas[operação]:
            string = str(op)
            print(f"\n\t{numA} {operação} {numB} =", "\033[34m" + string + "\033[0m")

    except:
        quit()