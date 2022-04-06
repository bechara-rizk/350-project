class packet:
    def __init__(self):
        self.username=None
        self.message=None

    def set_username(self, username):
        self.username=username

    def get_username(self):
        return self.username

    def set_message(self, message):
        self.message=message

    def get_message(self):
        return self.message

    def encode(self):
        encoding=self.username+"\n"+self.message
        return encoding.encode()
    
    def decode(self, encoding):
        string=encoding.decode()
        data=string.split("\n")
        new=packet()
        new.username=data[0]
        new.message=data[1]
        return new
