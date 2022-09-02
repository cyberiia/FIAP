# Par ou Ímpar!

print("Par ou Ímpar!\n")

def sep():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

try:
    núm = int(input("Número: "))
    if núm % 2 == 0:                       # Se o resto da divisão de {núm} por 2 for 0, então é par!
        print(f"Resposta: {núm} é par!")
    else:
        print(f"Resposta: {núm} é ímpar!") # Caso o resto da divisão não seja == 0, é ímpar!
    sep()
except:
    quit()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Primo Fast!

print("Números Primos!\n") # Programa do professor, está errado :S

try:
    núm = int(input("Insira um número: "))
    i = 2
    while i < núm or núm == 1:             # Enquanto 2 for menor que {núm} ou {núm} == 1...:
        if núm % i == 0 or núm == 1:       # Se o resto da divisão de {núm} por 1 for 0, então não é primo!
            print(f"{núm} não é primo")
            break
        i+=1                               # i = i+1   --->   nova_variável = antiga_variável + 1
    else:
        print(f"{núm} é primo")
    sep()
except:
    quit()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Raíz Quadrada!

print("Raíz Quadrada!\n")

try:
    núm = int(input("Raíz: √"))
    raíz = núm ** 0.5
    print(f"Resposta: √{núm} é {raíz:.1f}")
except:
    quit()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

x = 2

x+=1         # Abreviação de x + 1 = x  |  # old_var_x + 1 = new_var_x
x-=1         # x - 1 = x
x*=1         # x * 1 = x
x/=1         # x / 1 = x
x**=1        # x ** 1 = x

print(x)