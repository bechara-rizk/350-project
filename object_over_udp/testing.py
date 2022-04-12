import threading
import time

def idk1():
    input()

def idk2():
    time.sleep(1)
    print("\ridk2")

th1=threading.Thread(target=idk1)
th2=threading.Thread(target=idk2)

th1.start()
th2.start()