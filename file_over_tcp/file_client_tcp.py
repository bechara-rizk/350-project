from math import ceil
from socket import *
import time
import os


serverName = "127.0.0.1"
serverPort = 12000
chunk_size = 2048
sep="\n"
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

file_name = "test.txt"#input("Enter the name of the file: ")  # THE FILE TO BE SENT SHOULD BE IN THE SAME DIRECTORY AS THIS FILE
file_size = os.path.getsize(file_name)
file_type = file_name.split(".")[1]
hello_msg = file_name+sep+file_type+sep+str(file_size)
# print(hello_msg)
clientSocket.sendto(hello_msg.encode(), (serverName, serverPort)) # SENDING HELLO MESSAGE WHICH INCLUDES FILE NAME, TYPE AND SIZE



print("file size: ", file_size) # file size in bytes
nb_chunks = ceil(file_size/chunk_size) 
print("nb of chunks: ",nb_chunks)  # number of chunks to be sent



i = 1
# progress = tqdm.tqdm(range(file_size), f"Sending {file_name}", unit="B", unit_scale=True, unit_divisor=1024) # progress bar
with open(file_name, "rb") as file:

    time.sleep(0.1)
    while True:
        chunk = file.read(chunk_size)
        # progress.update(len(chunk))             # update progress bar
        if not chunk:
            print("file sent")
            break
        clientSocket.sendto(chunk,(serverName, serverPort))
        print("sent chunk size: ",len(chunk),"    ",i,"/",nb_chunks)
        i += 1
        

clientSocket.close() 