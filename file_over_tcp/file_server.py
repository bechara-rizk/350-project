"""
server side - receives files over UDP and saves them
"""


from socket import *

serverPort = 12000
chunk_size = 1024
chunks = []
sep="\n"

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("The server is ready to receive")

hello_rcvd = serverSocket.recv(2*chunk_size)
hello_rcvd = hello_rcvd.decode()
hello_rcvd = hello_rcvd.split(sep)
new_file = "new_"+hello_rcvd[0].split(".")[0]+"."+hello_rcvd[1]
print("new file name: ",new_file)

file = open(new_file, "wb")
while True:
    bytes_read = serverSocket.recv(2*chunk_size)
    chunks.append(bytes_read)
    print("received data chunk size: ",len(bytes_read))
    if (len(bytes_read) < chunk_size):
        input("file received, press enter to save it and exit")
        break
file.write(b''.join(chunks))
file.close()
serverSocket.close()
