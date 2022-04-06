from http import server
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


def receiver(port):
    serverPort=port
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))

    translator=base.packet()
    translator.set_username("Translator")
    status=base.packet()
    status.set_username("status")
    status.set_message("received successfully")

    print(f"Ready to receive on port {serverPort}.")
    while True:
        original_packet, clientAddress = serverSocket.recvfrom(2048)
        packet=translator.decode(original_packet)
        print(f"Received from {packet.username}: ",packet.get_message())
        serverSocket.sendto(status.encode(), clientAddress)

def sender(server_name,server_port,packet):
    translator=base.packet()
    translator.set_username("Translator")

    serverName=server_name
    serverPort=server_port
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.sendto(packet.encode(),(serverName, serverPort))

    status, serverAddress = clientSocket.recvfrom(2048)
    decoded_status=translator.decode(status)
    print(decoded_status.get_message())
    clientSocket.close()
