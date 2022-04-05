import json

class test:
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b

    def encode(self):
        encoding=str(self.a)+str(self.b)
        return encoding.encode()
    
    def decode(self, encoding):
        string=encoding.decode()
        new=test()
        new.a=int(string[0])
        new.b=int(string[1])
        return new
