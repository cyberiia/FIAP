# If Statements!

print("Sorveteria Kibom")
escolha = input("\nEscolha o sabor:\n • Limão\n • Chocolate\n • Creme\n • Flocos\n\n ➜ ")

sabores = ["Limão","Chocolate","Creme","Flocos"]    # Lista com valores válidos

# REMOVENDO CASE SENSITIVE

if escolha == escolha.lower():
    resposta = escolha[:1].upper() + escolha[1:]

elif escolha == escolha.upper():
    resposta = escolha[:1] + escolha[1:].lower()

if resposta in sabores:                              # Se a escolha estiver dentro dos valores válidos (respeitando acentuação)...:
    print(f"   {resposta}? Boa escolha!")

elif resposta not in sabores:                        # Ou apenas 'else' indicará que se o input estiver fora da lista 'sabores'...:
    print("   Não temos esse sabor :(")              # 'Not in' juntamente com if-elif irá verificar se a variável 'escolha' não está dentro da lista 'sabores'

print("\n~~~~~~~~~~~~~~~~~~~~~\n")#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# If com Múltiplas Condições!

print("Você pode dirigir?\n")
idade = int(input("Sua idade? "))
cnh = input("Possui CNH? (s/n) ")

if cnh == "s":
    cnh = True

if((cnh == True) and (idade >= 18)):           # Para a instrução abaixo ser executada, o IF recebe mais de uma condição e ambas devem retornar True
    print("Pode dirigir!")

else:
    print("Não pode dirigir.")


print("\n~~~~~~~~~~~~~~~~~~~~~\n")#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("\nIdentificador de Portas Lógicas\n")

while 1: # Loop para manter o programa rodando
    PortsIANA = {
        "21":["FTP","TCP"],
        "22":["SSH","TCP"],
        "23":["Telnet","TCP"],
        "25":["SMTP","TCP"],
        "53":["DNS","TCP, UDP"],
        "69":["TFTP","UDP"],
        "79":["Finger","TCP"],
        "80":["HTTP","TCP"],
        "110":["POP","TCP"],
        "143":["IMAP","TCP"],
        "389":["LDAP","TCP, UDP"],
        "443":["HTTPS","TCP, UDP"],
        "520":["RIP","UDP"],
        "2049":["NFS","TCP, UDP"],
        "3390":["RDP","TCP, UDP"],
        "6667":["IRCd","TCP"],
        "8080":["HTTP alt","TCP"]
    }

    port = input("Número da Porta: ")

    if port in PortsIANA:                                                           # Se o input estiver dentro do dicionário, executará a ação abaixo:
        print(f"Serviço: {PortsIANA[port][0]}\nProtocolo: {PortsIANA[port][1]}\n")  # Printará o primeiro elemento da lista, em seguida o segundo elemento.
    
    elif port == "q":
        break

    else:                                                                           # Se o input NÃO estiver dentro do dicionário...:
        print("Porta desconhecida\n")

    print("~~~~~~~~~~~~~~~~~~~~~\n")