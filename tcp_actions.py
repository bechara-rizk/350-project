from math import ceil
from socket import *
import magic # check the end of this code for library download commands 
import time
import os
#import tqdm
#from genericpath import getsize   
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
    #print("\n", file_type,"\n")
    new_hello = file_type.encode()
    # print(hello_msg)
    #clientSocket_tcp.send(hello_msg.encode()) # SENDING HELLO MESSAGE WHICH INCLUDES FILE NAME, TYPE AND SIZE
    



    print("file size: ", file_size) # file size in bytes
    nb_chunks = ceil(file_size/chunk_size) 
    print("nb of chunks: ",nb_chunks)  # number of chunks to be sent
    print("starting...")

    i = 0
    
    with open(file_name, 'rb') as read_file:   
        while i < nb_chunks:
            #print("sending chunk: ",i)
            read_file.seek(i*chunk_size)
            data = read_file.read(chunk_size)
            clientSocket_tcp.send(data)
            i += 1
            #print("sent chunk: ",i)
    read_file.close()
    print("file sent")
    clientSocket_tcp.send(new_hello)
    #clientSocket_tcp.close()
    #exit()
    #clientSocket_tcp.close()
    # progress = tqdm.tqdm(range(file_size), f"Sending {file_name}", unit="B", unit_scale=True, unit_divisor=1024) # progress bar
    #while True:
        #conn, addr = s.accept()     # Establish connection with client.
        #print ('Got connection from', addr)
        #data = conn.recv(2048)
        #print('Server received', repr(data))

        #filename='test1.pdf' #In the same folder or path is this file running must the file you want to tranfser to be
    """ file = open(file_name,'rb')
        l = file.read(chunk_size)
        while (l):
            clientSocket_tcp.send(l)
        #print('Sent ',repr(l))
        l = file.read(chunk_size)
        file.close()
 """
     #   print('Done sending')
        #conn.send(('Thank you for connecting').encode())
      # clientSocket_tcp.close()
        #clientSocket_tcp.close() 


# FILE SENDER END


#################################################################################


# FILE RECEIVER START

def file_receiver(receiverName, receiverPort):
    file_receiver.y = 0     # file index
    chunk_size = 2048

    sep="\n"
    #chunks=[]

    serverSocket_tcp = socket(AF_INET, SOCK_STREAM)
    serverSocket_tcp.bind(('', receiverPort))
    serverSocket_tcp.listen(1)
    print("The server is ready to receive")
    
    def receive_file():
        connectionSocket, addr = serverSocket_tcp.accept()
        
        
        #hello_rcvd = connectionSocket.recv(chunk_size)
        #hello_rcvd = hello_rcvd.decode()
        # print(getsizeof(hello_rcvd))
        #hello_rcvd = hello_rcvd.split(sep)
        #new_file = "new_"+hello_rcvd[0].split(".")[0]+"."+hello_rcvd[1]
        #print("you will be receiving a file from ",hello_rcvd[3])
        #print("file name in your machine: ",new_file)
        new_file = "new_file"
        with open(new_file, 'wb') as f:
            while True:
                
                data = connectionSocket.recv(chunk_size)
                if not data:
                    break
                f.write(data)
            #print("received data: ",data.decode())
        

            #progress = tqdm.tqdm(range(int(hello_rcvd[2])), f"Receiving {hello_rcvd[0]}", unit="B", unit_scale=True, unit_divisor=1024)
        """ with open(new_file, 'wb') as f:
                print ('file opened')
                while True:
                    #print('receiving data...')
                    data = connectionSocket.recv(chunk_size)
                    #print('data=%s', (data))
                    if not data:
                        break
                    # write data to a file
                    f.write(data) """
            #f.close()
            #print('Successfully get the file')
        """ connectionSocket.close()
            serverSocket_tcp.close() """
        print('\nfile received')
        time.sleep(1)
        #print("received hello: ",my_hello)
        connectionSocket.close()
        #serverSocket_tcp.close()
        
        #print(magic.from_file(new_file, mime=True))
        rep_ind = "("+str(file_receiver.y)+")"
        file_receiver.y+=1

        if (magic.from_file(new_file, mime=True) == "application/pdf"):
            os.rename(new_file, "new_pdf"+rep_ind+".pdf")
        elif (magic.from_file(new_file, mime=True) == "image/jpeg"):
            os.rename(new_file, "new_jpg"+rep_ind+".jpg")
        elif(magic.from_file(new_file, mime=True) == "image/png"):
            os.rename(new_file, "new_png"+rep_ind+".png")
        elif(magic.from_file(new_file, mime=True) == "image/gif"):
            os.rename(new_file, "new_gif"+rep_ind+".gif")
        elif(magic.from_file(new_file, mime=True) == "text/plain"):
            os.rename(new_file, "new_txt"+rep_ind+".txt")
        elif(magic.from_file(new_file, mime=True) == "application/msword"):
            os.rename(new_file, "new_doc"+rep_ind+".doc")
        elif(magic.from_file(new_file, mime=True) == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"):
            os.rename(new_file, "new_docx"+rep_ind+".docx")
        elif(magic.from_file(new_file, mime=True) == "application/vnd.ms-excel"):
            os.rename(new_file, "new_xls"+rep_ind+".xls")
        elif(magic.from_file(new_file, mime=True) == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"):
            os.rename(new_file, "new_xlsx"+rep_ind+".xlsx")
        elif(magic.from_file(new_file, mime=True) == "application/vnd.ms-powerpoint"):
            os.rename(new_file, "new_ppt"+rep_ind+".ppt")
        elif(magic.from_file(new_file, mime=True) == "application/vnd.openxmlformats-officedocument.presentationml.presentation"):
            os.rename(new_file, "new_pptx"+rep_ind+".pptx")
        elif(magic.from_file(new_file, mime=True) == "application/python"):
            os.rename(new_file, "new_py"+rep_ind+".py")
        
    #exit()
        receive_file()
    #file_receiver(receiverName, receiverPort)    # RECURSIVE FUNCTION CALL
    receive_file()