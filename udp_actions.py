from socket import *
import udp_base
import random
import sys

def display_message(packet):
    print(f">>>{packet.get_username()}: ",packet.get_message())

def receiver(port):
    serverPort=port
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))

    print(f"Ready to receive on port {serverPort}.")

    received=None

    while True:
        status=udp_base.packet()
        status.set_username("status")
        original_packet, clientAddress = serverSocket.recvfrom(2048)
        packet=udp_base.packet().decode(original_packet)
        if packet.corrupted:
            status.ack_flag=False
        else:
            status.ack_flag=True
            if received!=packet.seq_nb:
                display_message(packet)
                status.ack_nb=received=packet.seq_nb
            else:
                status.ack_nb=received
        serverSocket.sendto(status.encode(), clientAddress)


def sender(serverName, serverPort,packet):
    # packet.syn_flag=True
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    packet.seq_nb=random.randint(0,1000000000000)
    timeOut=0.1
    clientSocket.settimeout(timeOut)
    # while True:
    #     message=
    #     if message=="":
    #         continue
    #     elif len(message)<=2048:
    #         break
    #     print("Message too long, try again with a shorter message.")
    # packet.set_message(message)
    while True:
        clientSocket.sendto(packet.encode(),(serverName, serverPort))
        try:
            status, serverAddress = clientSocket.recvfrom(2048)
            status=udp_base.packet().decode(status)
            if not status.ack_flag or status.corrupted:
                clientSocket.sendto(packet.encode(),(serverName, serverPort))
            else:
                packet.seq_nb+=1
                break
        except:
            timeOut+=0.1
            clientSocket.settimeout(timeOut)
            pass #keep sending the packet until it is received
