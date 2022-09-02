from socket import *
serverPort = 12500                         # Porta do servidor
serverSocket = socket(AF_INET, SOCK_DGRAM) # AF_NET (IPv4), SOCK_DGRAM (UDP)
serverSocket.bind(("", serverPort))        # Abre a porta, especificando o IP
print ("UDP server\n")                     # Camada de apresentação, codificação dos dados

while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    text = str(message,"utf-8") #cp1252 #utf-8
    print ("Received from Client: ", text)