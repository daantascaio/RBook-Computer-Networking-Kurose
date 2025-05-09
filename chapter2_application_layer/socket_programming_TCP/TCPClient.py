from socket import *  # Importa todas as classes e funções do módulo 'socket'


# Nome ou endereço IP do servidor ao qual o cliente irá se conectar
serverName = 'servername'
serverPort = 12000  # Porta na qual o servidor está escutando conexões

clientSocket = socket(AF_INET, SOCK_STREAM)  # Cria um socket TCP usando IPv4

# Estabelece a conexão com o servidor especificado
clientSocket.connect((serverName, serverPort))


# Lê uma frase em letras minúsculas do usuário
sentence = input('Input lowercase sentence: ')


# Codifica a string para bytes e envia ao servidor
clientSocket.send(sentence.encode())

# Recebe até 1024 bytes da resposta do servidor
modifiedSentence = clientSocket.recv(1024)


# Decodifica a resposta recebida e imprime
print('From Server: ', modifiedSentence.decode())
clientSocket.close()  # Fecha o socket, encerrando a conexão com o servidor
