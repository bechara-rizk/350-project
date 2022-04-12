import base
import actions
import threading

peer1_port=12001
peer2_port=12002

channel_name="127.0.0.1"


packet=base.packet()
username="peer2" #input("Input your username: ")
packet.set_username(username)

def chat():
    #actions.init_connection(channel_name,peer1_port)
    while True:
        while True:
            message=input("Enter your message: ")
            if message.length()<=2048:
                break
            print("Message too long, try again with a shorter message.")
        packet.set_message(message)
        actions.sender(channel_name,peer1_port,packet)

chatter=threading.Thread(target=chat)
receiver=threading.Thread(target=actions.receiver,args=(peer2_port,))
receiver.start()
chatter.start()