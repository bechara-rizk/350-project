from gettext import translation
import base
import json
from socket import *

test=base.test(2,3)
translator=base.test()

message=test.encode()

serverName = "127.0.0.1"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
modifiedMessage=modifiedMessage.decode()
modifiedMessage=translator.decode(modifiedMessage)
print(modifiedMessage)
clientSocket.close()