from socket import *
serverName = "127.0.0.1" # ::1 IPv6 localhost
serverPort = 12500
clientSocket = socket(AF_INET, SOCK_DGRAM)
print("UDP Client\n")

while 1:
    message = input("Input message: ")
    if message == "exit":
            break
    clientSocket.sendto(bytes(message,"utf-8"), (serverName, serverPort))
clientSocket.close()