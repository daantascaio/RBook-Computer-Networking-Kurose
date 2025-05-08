from socket import *  # importa o módulo base para comunicação de rede em Python

serverPort = 12000  # define a porta onde o servidor vai escutar por mensagens

serverSocket = socket(AF_INET, SOCK_DGRAM)  # cria o socket do servidor
# AF_INET = usa IPv4
# SOCK_DGRAM = tipo UDP

serverSocket.bind(('', serverPort))  # vincula o socket à porta especificada
# '' significa que aceita conexões de qualquer IP

# exibe mensagem informando que o servidor está pronto
print("The server is ready to receive")

while True:  # laço infinito para manter o servidor sempre ouvindo
    # recebe mensagem do cliente (até 2048 bytes)
    message, clientAddress = serverSocket.recvfrom(2048)
    # guarda o texto e o endereço do cliente

    # decodifica a mensagem recebida e transforma em maiúsculas
    modifiedMessage = message.decode().upper()

    # envia a mensagem modificada de volta para o cliente
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
