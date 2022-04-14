import base
import actions
import threading
from socket import *


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

    actions.sender(channel_name,peer2_port,packet)