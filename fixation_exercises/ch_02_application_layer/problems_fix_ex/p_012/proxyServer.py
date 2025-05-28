from socket import *


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('The server is ready to receive, mother fucker!')

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f'\n Recebi uma conexão de {addr}\n')

    request = connectionSocket.recv(4096).decode()

    print('====== Resquest accept ======')
    print(request)
    print('=============================')

    response = "HTTP/1.1 200 OK\r\n"
    response += "Content-Type: text/html\r\n\r\n"
    response += "<html><body><h1>Proxy funcionando</h1><body></html>\r\n"

    connectionSocket.send(response.encode())
    connectionSocket.close()
