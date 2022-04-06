import base
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

translator=base.packet("translator")

print("The server is ready to receive")
while True:
    original_message, clientAddress = serverSocket.recvfrom(2048)
    message=translator.decode(original_message)
    print(f"Received from {message.username}: ",message.get_message())
    message.set_message("hello world from server")
    serverSocket.sendto(message.encode(), clientAddress)