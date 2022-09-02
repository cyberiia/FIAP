# Criptografia Simétrica!

# Cifra de Atbash
print('Atbash Cipher\n')

tabela = {'A' : 'Z', 'B' : 'Y', 'C' : 'X',
          'D' : 'W', 'E' : 'V', 'F' : 'U',
          'G' : 'T', 'H' : 'S', 'I' : 'R',
          'J' : 'Q', 'K' : 'P', 'L' : 'O',
          'M' : 'N', 'N' : 'M', 'O' : 'L',
          'P' : 'K', 'Q' : 'J', 'R' : 'I',
          'S' : 'H', 'T' : 'G', 'U' : 'F',
          'V' : 'E', 'W' : 'D', 'X' : 'C'}

def atbash(message):
    cipher = ''
    for letter in message:
        if(letter != ' '):           # Checa se há espaços
            cipher += tabela[letter] # Adiciona a letra correspondente a cifra
        else:
            cipher += ' '            # Adiciona espaços
  
    return cipher
  
def main():                 
    message = 'GEEKS FOR GEEKS'    # Encripta a mensagem
    print(atbash(message.upper()))
      
    message = 'TVVPH ULI TVVPH'    # Decripta a mensagem
    print(atbash(message.upper()))
  
if __name__ == '__main__':         # Roda a função main()
    main()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Cifra de César

import string

print('\nCaesar Cipher\n')
message = input('Insert the message: ') # Entrar com a mensagem
message = message.lower()               # Transforma letras maiúsculas em minúsculas
key = int(input('Insert the key: '))    # Chave para rotacionar
alfabet = list(string.ascii_lowercase)  # Lista todas as letras minúsculas do alfabeto
result = ''

for letters in message:                     # Para cada letra na mensagem
    if letters in alfabet:                  # Se as letras estiverem dentro do alfabeto
        position = alfabet.index(letters)   # Localiza os valores das posições das letras no alfabeto
        position = (position + key) % 26    # Fará a rotação, 26 é o total de letras do alfabeto
        result = result + alfabet[position] # Nova posição da letra após a rotação
print(f'Result: {result}')