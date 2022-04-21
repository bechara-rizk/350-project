from socket import *

serverPort = 12000
chunk_size = 2048

sep="\n"
chunks=[]

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
connectionSocket, addr= serverSocket.accept()

hello_rcvd = connectionSocket.recv(chunk_size)
hello_rcvd = hello_rcvd.decode()
hello_rcvd = hello_rcvd.split(sep)
#new_file = "new_"+hello_rcvd[0].split(".")[0]+"."+hello_rcvd[1]
new_file = "new_test.txt"
print("new file name: ",new_file)

file = open(new_file, "wb")
# print(hello_rcvd)
while True:
    bytes_read = connectionSocket.recv(chunk_size)
    # print(bytes_read)
    chunks.append(bytes_read)
    if (len(bytes_read) < chunk_size):
        break
    else:
        chunks.append(bytes_read)
   # print("received data chunk size: ",len(bytes_read))
    
file.write(b''.join(chunks))

file.close()
print("file received or connection closed before completion, check above")
