import json

class test:
    def __init__(self,a=0,b=0) -> None:
        self.a=a
        self.b=b

    def encode(self):
        encoding=str(self.a)+str(self.b)
        return encoding
    
    def decode(self, encoding):
        new=test()
        test.a=int(encoding[0])
        test.b=int(encoding[1])
        return test
