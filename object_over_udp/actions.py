from socket import *
import base
import threading
import time

def display_message(packet):
    print(f">>>{packet.get_username()}: ",packet.get_message())

def receiver(port):
    serverPort=port
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))

    # translator=base.packet()
    # translator.set_username("Translator")

    received=None

    print(f"Ready to receive on port {serverPort}.")

    while True:
        status=base.packet()
        status.set_username("status")
        original_packet, clientAddress = serverSocket.recvfrom(2048)
        #print(clientAddress)
        packet=base.packet().decode(original_packet)
        received=packet.seq_nb
        #status.ack_nb=received
        if packet.syn_flag and (not packet.corrupted):
            print(f"{packet.get_username()} is connected.")
            status.ack_flag=True
            status.syn_flag=True
        else:
            if packet.corrupted:
                status.ack_flag=False
            else:
                status.ack_flag=True
                if status.ack_nb!=received:
                    display_message(packet)
                status.ack_nb=received
        #print("ack sent")
        serverSocket.sendto(status.encode(), clientAddress)


def chat(serverName, serverPort,packet):
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

def wrapper(clientSocket,returns):
    status, serverAddress = clientSocket.recvfrom(2048)
    returns[0]=status


def init_connection(server_name,server_port):
    connection=[False]
    packet=base.packet()
    packet.set_username("init")
    packet.set_message("init")
    packet.syn_flag=True
    returns=[False]
    timeout=threading.Thread(target=timer,args=(5,returns))
    sending=threading.Thread(target=wrapper)
    timeout.start()
    while not connection[0] and not returns[0]:
        pass
    if connection[0]:
        return True
    if returns[0]:
        return False

def timer(timeout=5,broken=[False]):
    count=0
    while count<timeout:
        time.sleep(0.005)
        count+=0.005
    broken[0]=True
