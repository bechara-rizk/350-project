import hashlib

class packet:
    def __init__(self):
        self.username="nDef"
        self.message="nDef"
        self.checksum="nDef"
        self.corrupted=False
        self.ack_flag=False
        self.syn_flag=False
        self.ack_nb=0
        self.seq_nb=0
        self.fin_flag=False
        # self.timing=100
        # self.breaker=False
    
    # def timer(self,timeout=5,broken=[False]):
    #     count=0
    #     while count<timeout and not self.breaker:
    #         time.sleep(0.005)
    #         count+=0.005
    #     broken[0]=True
    #     return True

    def set_username(self, username):
        self.username=username

    def get_username(self):
        return self.username

    def set_message(self, message):
        self.message=message

    def get_message(self):
        return self.message

    def encode(self):
        sep="\n"
        encoding=self.username+sep+self.message+sep+self.checksum+sep+str(self.ack_flag)+sep+str(self.syn_flag)+sep+str(self.ack_nb)+sep+str(self.seq_nb)+sep+str(self.fin_flag)
        encoding=encoding.encode()
        self.generate_checksum(encoding)
        return encoding
    
    def decode(self, encoding):
        try:
            string=encoding.decode()
            data=string.split("\n")
            new=packet()
            new.username=data[0]
            new.message=data[1]
            new.checksum=data[2]
            new.ack_flag=self.str_to_bool(data[3])
            new.syn_flag=self.str_to_bool(data[4])
            new.ack_nb=int(data[5])
            new.seq_nb=int(data[6])
            new.fin_flag=self.str_to_bool(data[7])
            self.corrupted=not(self.verify_checksum(encoding))
            return new
        except: #any error while decoding says that the packet is corrupted
            self.corrupted=True
        # except:
        #     pass

    def str_to_bool(self,string):
        if string=="True":
            return True
        else:
            return False

    def generate_checksum(self,encoding):
        self.checksum=hashlib.md5(encoding).hexdigest()
    
    def verify_checksum(self,encoding):
        return self.checksum==hashlib.md5(encoding).hexdigest()
