import base
from socket import *

test=base.packet("bechara")
test.set_message(input("enter message: "))
translator=base.packet("translator")


serverName = "127.0.0.1"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto(test.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
decoded_message=translator.decode(modifiedMessage)
print(decoded_message.get_message())
clientSocket.close()