from socket import *
import base

def start_receiver(message):
    test=base.packet("bechara")
    test.set_message(message)
    translator=base.packet("translator")
    serverName = "127.0.0.1"
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.sendto(test.encode(),(serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    decoded_message=translator.decode(modifiedMessage)
    print(decoded_message.get_message())
    clientSocket.close()

def start_sender():
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