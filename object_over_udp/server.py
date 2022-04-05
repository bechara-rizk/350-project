import base
import json
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
translator=base.test()
print("The server is ready to receive")
while True:
    original_message, clientAddress = serverSocket.recvfrom(2048)
    message=translator.decode(original_message)
    print("Received: ",message)
    message.a+=1
    message.b*=2
    #encoded=message.encode(message)
    serverSocket.sendto(message.encode(), clientAddress)