from socket import *

serverPort = 12000
chunk_size = 1024
chunks = []
sep="\n"

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("The server is ready to receive")
rec_type = serverSocket.recv(2*chunk_size)
rec_type = rec_type.decode()
rec_type = rec_type.split(sep)
new_file = "new_file."+rec_type[1]

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