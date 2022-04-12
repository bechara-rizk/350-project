import base
import actions
import threading
from socket import *

def chat3(serverName, serverPort,packet):
    packet.syn_flag=True
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    packet.seq_nb=0
    clientSocket.sendto(packet.encode(),(serverName, serverPort))
    clientSocket.settimeout(10)
    try:
        status, serverAddress = clientSocket.recvfrom(2048)
        status=base.packet().decode(status)
        if status.ack_flag and status.syn_flag and not status.corrupted:
            print("Connected to peer.")
            packet.syn_flag=False
        else:
            print("Connection failed.")
            return
    except:
        print("Server is not accepting connections.")
        return
    packet.seq_nb+=1
    while True:
        while True:
            message=input("Enter your message: ")
            if len(message)<=2048:
                break
            print("Message too long, try again with a shorter message.")
        packet.set_message(message)
        while True:
            #actions.sender(clientSocket,channel_name,peer2_port,packet)
            clientSocket.sendto(packet.encode(),(serverName, serverPort))
            try:
                status, serverAddress = clientSocket.recvfrom(2048)
                status=base.packet().decode(status)
                if not status.ack_flag or status.corrupted:
                    clientSocket.sendto(packet.encode(),(serverName, serverPort))
                else:
                    packet.seq_nb+=1
                    break
            except:
                #print("im in except")
                pass #keep sending the packet until it is received
                # print("Server disconnected.")
                # return

def menu():
    text="""Welcome to HTTB!
    Enter 1 to connect to peer.
    Then enter any text to send to peer.
    Enter 2 to disconnect.
    """
    print(text)
    choice=input("Enter your choice: ")
    return choice

if __name__=="__main__":
    peer1_port=12001
    peer2_port=12002

    channel_name="127.0.0.1"

    packet=base.packet()
    username="peer1" #input("Input your username: ")
    packet.set_username(username)

    #choice=menu()

    actions.chat(channel_name,peer2_port,packet)