import base
import actions
import threading
from socket import *
import time

if __name__=="__main__":
    peer1_port=12001
    peer2_port=12002

    channel_name="127.0.0.1"

    packet=base.packet()
    username=input("Input your username: ")
    # username="p2"
    packet.set_username(username)

    rec=threading.Thread(target=actions.receiver,args=(peer2_port,))
    rec.start()
    time.sleep(0.5)
    while True:
        send=threading.Thread(target=actions.sender,args=(channel_name,peer1_port,packet))
        input("Press enter to start sending and then input ur message and press enter again to send\n")
        send.start()
        send.join()
