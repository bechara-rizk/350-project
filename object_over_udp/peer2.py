from numpy import rec
import base
import actions
import threading

peer1_port=12001
peer1_name="127.0.0.1"

peer2_port=12002
peer2_name="127.0.0.1"

packet=base.packet()
username="peer2" #input("Input your username: ")
packet.set_username(username)

def chat():
    while True:
        message=input("Input your message: ")
        packet.set_message(message)
        actions.sender(peer1_name,peer1_port,packet)

chatter=threading.Thread(target=chat)
receiver=threading.Thread(target=actions.receiver,args=(peer2_port,))
chatter.start()
receiver.start()