import threading
import time

def idk1():
    a=None
    a=input()
    print("idk1",a)
    return

def idk2():
    time.sleep(1)
    print("idk2")

th2=threading.Thread(target=idk2)

th2.start()

while True:
    th1=threading.Thread(target=idk1)
    th1.start()
    th1.join()
    print("out")