from socket import * # é um modulo de base para todas as comunicações de rede em python

serverName = 'hostname' # o valor dessa variável ou é o IP (168.135.12.50) ou é um hostname do servidor (cis.poly.edu) 
                        #usando o hostname, será realizada uma consulta DNS para obter o endereço IP

serverPort = 12000  # define o valor da var int

clientSocket = socket(AF_INET, SOCK_DGRAM) # está linha cria o socket do cliente: AF_INET significa que é um endereço
                                           # IPv4, SOCK_DGRAM significa que é um socket UDP 

message = input('Input lowercase sentence:') # input é um função que pede ao usuário que digite algo

clientSocket.sendto(message.encode(),(serverName, serverPort)) # sento() = usado para enviar dados via UDP
                                                               # encode() = transforma string em bytes

modifiedMessage, serverAddress = clientSocket.recvfrom(2048) # a mensagem é armazenada na var modifiedMessage
                                                             # o IP e a porta é armazenado no serverAddress

print(modifiedMessage.decode()) # printa na tela a mensagem

clientSocket.close() # fecha a comunicação
