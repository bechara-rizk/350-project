from socket import *
import base

def display_message(packet):
    print(f">>>{packet.get_username()}: ",packet.get_message())

def receiver(port):
    serverPort=port
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))

    print(f"Ready to receive on port {serverPort}.")

    received=None

    while True:
        status=base.packet()
        status.set_username("status")
        original_packet, clientAddress = serverSocket.recvfrom(2048)
        packet=base.packet().decode(original_packet)
        if packet.syn_flag and (not packet.corrupted):
            if received is None:
                print(f"{packet.get_username()} is online.")
            status.ack_nb=received=packet.seq_nb
            status.ack_flag=True
            status.syn_flag=True
        else:
            if packet.corrupted:
                status.ack_flag=False
            else:
                status.ack_flag=True
                if received is None:
                    received=packet.seq_nb-1
                elif received+1==packet.seq_nb:
                    if not packet.fin_flag:
                        display_message(packet)
                        status.ack_nb=received=packet.seq_nb
                    else:
                        print(f"{packet.get_username()} is not online anymore.")
                        status.ack_flag=False
                        status.syn_flag=False
                        status.fin_flag=False
                        status.ack_nb=received=None
                else:
                    status.ack_nb=received
        serverSocket.sendto(status.encode(), clientAddress)


def sender(serverName, serverPort,packet):
    packet.syn_flag=True
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    packet.seq_nb=0
    clientSocket.settimeout(0.5)
    while True:
        clientSocket.sendto(packet.encode(),(serverName, serverPort))
        try:
            status, serverAddress = clientSocket.recvfrom(2048)
            status=base.packet().decode(status)
            if status.ack_flag and status.syn_flag and not status.corrupted:
                print("You are online.")
                packet.syn_flag=False
                break
            else:
                continue
        except timeout:
            continue
    packet.seq_nb+=1
    while True:
        while True:
            message=input()
            if message=="":
                continue
            elif len(message)<=2048:
                break
            print("Message too long, try again with a shorter message.")
        packet.set_message(message)
        if message=="2":
            packet.fin_flag=True
            clientSocket.sendto(packet.encode(),(serverName, serverPort))
            packet.fin_flag=False
            return
        while True:
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
                pass #keep sending the packet until it is received