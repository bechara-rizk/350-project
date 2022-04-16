"""
Sending a file over UDP
Tested for: .txt , .py , .pdf , .docx , .png
"""

from socket import *
import os
import time
from math import ceil

serverName = "127.0.0.1"
serverPort = 12000
chunk_size = 1024
sep="\n"

file_name = "my_text.txt"                                          # THE FILE TO BE SENT SHOULD BE IN THE SAME DIRECTORY AS THIS FILE

file_size = os.path.getsize(file_name)

clientSocket = socket(AF_INET, SOCK_DGRAM)
file_type = input("Enter file type: py, txt, docx, pdf ..?: ")
hello_msg = file_name+sep+file_type+sep+str(file_size)

clientSocket.sendto(hello_msg.encode(), (serverName, serverPort)) # SENDING HELLO MESSAGE WHICH INCLUDES FILE NAME, TYPE AND SIZE
time.sleep(2)                                                     # give some time for the server to create the file (will be removed later in TCP)


print("file size: ", file_size) # file size in bytes
nb_chunks = ceil(file_size/chunk_size) 
print("nb of chunks: ",nb_chunks)  # number of chunks to be sent

# time.sleep(5)  


i = 1
with open(file_name, "rb") as file:
    while True:
        chunk = file.read(chunk_size)
        if not chunk:
            input("file sent, press enter to exit")
            break
        clientSocket.sendto(chunk,(serverName, serverPort))
        print("sent chunk size: ",file_size,"    ",i,"/",nb_chunks)
        i += 1
        

clientSocket.close() 
