import base
import actions
import threading


sender=threading.Thread(target=actions.start_sender)
receiver=threading.Thread(target=actions.start_receiver,args=(input("enter message: "),))
receiver.start()