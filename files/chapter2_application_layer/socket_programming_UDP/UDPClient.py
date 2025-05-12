from socket import *  # importa o módulo base para comunicação de rede em Python

# pode ser um IP (ex: 168.135.12.50) ou um nome de domínio (ex: cis.poly.edu)
serverName = 'localhost'
# se for um hostname, o sistema faz uma busca DNS para descobrir o IP

serverPort = 12000  # define a porta que será usada para enviar a mensagem

clientSocket = socket(AF_INET, SOCK_DGRAM)  # cria o socket do cliente
# AF_INET = usa IPv4
# SOCK_DGRAM = tipo de socket UDP

# pede pro usuário digitar uma frase em letras minúsculas
message = input('Input lowercase sentence: ')

# envia a mensagem codificada (em bytes) para o servidor
clientSocket.sendto(message.encode(), (serverName, serverPort))
# sendto() é usado com sockets UDP

modifiedMessage, serverAddress = clientSocket.recvfrom(
    2048)  # recebe a resposta do servidor (até 2048 bytes)
# guarda a mensagem modificada e o endereço do servidor

# exibe a resposta do servidor já decodificada (voltando de bytes pra string)
print(modifiedMessage.decode())

clientSocket.close()  # encerra a conexão do socket
