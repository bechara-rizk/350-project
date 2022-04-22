import threading
from socket import *
import time
import actions_tcp


if __name__=="__main__":

    peer1_tcp_port=12003
    peer2_tcp_port=12004

    channel_name="127.0.0.1"

    

    rec=threading.Thread(target=actions_tcp.file_receiver,args=(channel_name, peer1_tcp_port))  # receiving files on port 12003
    rec.start()
    time.sleep(0.5)
    while True:
        send=threading.Thread(target=actions_tcp.file_sender,args=(channel_name,peer2_tcp_port)) # sending files to port 12004
        input("Press enter to start sending")  # will be replaced by a button in the GUI
        send.start()
        send.join()
