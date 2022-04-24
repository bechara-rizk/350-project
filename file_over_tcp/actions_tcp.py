from math import ceil
from socket import *
# import time
import os
# import tqdm
from genericpath import getsize         # used for hello_msg
# from sys import getsizeof

def file_sender(receiverName, receiverPort):
    
    chunk_size = 2048
    sep="\n"


    clientSocket_tcp = socket(AF_INET, SOCK_STREAM)
    clientSocket_tcp.connect((receiverName,receiverPort))

    while True:
        file_name = input("Enter the name of the file: ")
        if os.path.isfile(file_name):
            break
        else:
            print("file does not exist")
    file_size = os.path.getsize(file_name)
    file_type = file_name.split(".")[1]
    username = input("Enter your username: ")
    hello_msg = file_name+sep+file_type+sep+str(file_size)+sep+username
    # print(hello_msg)
    clientSocket_tcp.sendto(hello_msg.encode(), (receiverName, receiverPort)) # SENDING HELLO MESSAGE WHICH INCLUDES FILE NAME, TYPE AND SIZE



    print("file size: ", file_size) # file size in bytes
    nb_chunks = ceil(file_size/chunk_size) 
    print("nb of chunks: ",nb_chunks)  # number of chunks to be sent
    print("starting...")

    i = 1
    # progress = tqdm.tqdm(range(file_size), f"Sending {file_name}", unit="B", unit_scale=True, unit_divisor=1024) # progress bar
    with open(file_name, "rb") as file:
        while True:
            chunk = file.read(chunk_size)
            # progress.update(len(chunk))             # update progress bar
            if not chunk:
                print("file sent")
                break
            clientSocket_tcp.sendto(chunk,(receiverName, receiverPort))
            # print("sent chunk size: ",len(chunk),"    ",i,"/",nb_chunks)
            i += 1
            
    file.close()
    #clientSocket_tcp.close() 


# FILE SENDER END


#################################################################################


# FILE RECEIVER START

def file_receiver(receiverName, receiverPort):

    chunk_size = 2048

    sep="\n"
    chunks=[]

    serverSocket_tcp = socket(AF_INET, SOCK_STREAM)
    # print(receiverPort)
    serverSocket_tcp.bind(('', receiverPort))
    serverSocket_tcp.listen(1)
    print("The server is ready to receive")
    connectionSocket, addr= serverSocket_tcp.accept()
    hello_rcvd = connectionSocket.recv(chunk_size)
    hello_rcvd = hello_rcvd.decode()
    # print(getsizeof(hello_rcvd))
    hello_rcvd = hello_rcvd.split(sep)
    new_file = "new_"+hello_rcvd[0].split(".")[0]+"."+hello_rcvd[1]
    print("you will be receiving a file from ",hello_rcvd[3])
    print("file name in your machine: ",new_file)

    file = open(new_file, "wb")
    # progress = tqdm.tqdm(range(int(hello_rcvd[2])), f"Receiving {hello_rcvd[0]}", unit="B", unit_scale=True, unit_divisor=1024)
    while True:
        bytes_read = connectionSocket.recv(chunk_size)
        chunks.append(bytes_read)
        if (len(bytes_read) < chunk_size):
            # progress.close()
            break
        # else:
        #     progress.update(len(bytes_read))             # update progress bar
    # print("received data chunk size: ",len(bytes_read))
    file.write(b''.join(chunks))
    file.close()
    print("file received or connection closed before completion, check above")
    connectionSocket.close()
    serverSocket_tcp.close()
    file_receiver(receiverName, receiverPort)    # RECURSIVE FUNCTION CALL
