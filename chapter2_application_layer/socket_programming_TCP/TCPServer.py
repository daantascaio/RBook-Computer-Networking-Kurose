# Importa todas as funções e classes do módulo 'socket' para comunicação de rede
from socket import *

serverPort = 12000  # Define a porta na qual o servidor vai escutar conexões

# Cria um socket TCP (SOCK_STREAM) usando IPv4 (AF_INET)
serverSocket = socket(AF_INET, SOCK_STREAM)

# Associa o socket a todas as interfaces locais e à porta definida
serverSocket.bind(('', serverPort))

# Coloca o socket em modo de escuta, permitindo até 1 conexão pendente
serverSocket.listen(1)

# Mensagem indicando que o servidor está pronto
print('The server is ready to receive')

while True:  # Loop infinito para atender conexões continuamente
    # Aceita uma nova conexão; retorna um novo socket e o endereço do cliente
    connectionSocket, addr = serverSocket.accept()

    # Recebe até 1024 bytes de dados e decodifica de bytes para string
    sentence = connectionSocket.recv(1024).decode()

    # Converte a string recebida para letras maiúsculas
    capitalizedSentence = sentence.upper()

    # Codifica a string modificada e envia de volta ao cliente
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()  # Encerra a conexão com o cliente atual
