from tkinter import *
from tkinter import font
from tkinter import ttk
import threading
import udp_base
import udp_actions
from socket import *
import udp_base

#taken from geeksforgeeks.org and adapted for our code
"https://www.geeksforgeeks.org/gui-chat-application-using-tkinter-in-python/"

class GUI:
    # constructor method
    def __init__(self):
        self.channel_name = "127.0.0.1"
        self.udp_p1_port = 12001
        self.udp_p2_port = 12002
        self.tcp_p1_port = 12003
        self.tcp_p2_port = 12004
        self.packet=udp_base.packet()
       
        # chat window which is currently hidden
        self.Window = Tk()
        self.Window.withdraw()
         
        # login window
        self.login = Toplevel()
        # set the title
        self.login.title("Login")
        self.login.resizable(width = False,
                             height = False)
        self.login.configure(width = 400,
                             height = 300)
        # create a Label
        self.pls = Label(self.login,
                       text = "Please login to continue",
                       justify = CENTER,
                       font = "Helvetica 14 bold")
         
        self.pls.place(relheight = 0.15,
                       relx = 0.2,
                       rely = 0.07)
        # create a Label
        self.labelName = Label(self.login,
                               text = "Name: ",
                               font = "Helvetica 12")
         
        self.labelName.place(relheight = 0.2,
                             relx = 0.1,
                             rely = 0.2)
         
        # create a entry box for
        # tyoing the message
        self.entryName = Entry(self.login,
                             font = "Helvetica 14")
         
        self.entryName.place(relwidth = 0.4,
                             relheight = 0.12,
                             relx = 0.35,
                             rely = 0.2)
         
        # set the focus of the cursor
        self.entryName.focus()
         
        # create a Continue Button
        # along with action
        self.go = Button(self.login,
                         text = "CONTINUE",
                         font = "Helvetica 14 bold",
                         command = lambda: self.goAhead(self.entryName.get()))
         
        self.go.place(relx = 0.4,
                      rely = 0.55)
        self.Window.mainloop()
 
    def goAhead(self, name):
        self.login.destroy()
        self.layout(name)
         
        # the thread to receive messages
        self.packet.set_username(name)
        udp_rec = threading.Thread(target=self.receive)
        udp_rec.start()
 
    # The main layout of the chat
    def layout(self,name):
       
        self.name = name
        # to show chat window
        self.Window.deiconify()
        self.Window.title("CHATROOM")
        self.Window.resizable(width = False,
                              height = False)
        self.Window.configure(width = 470,
                              height = 550,
                              bg = "#17202A")
        self.labelHead = Label(self.Window,
                             bg = "#17202A",
                              fg = "#EAECEE",
                              text = self.name ,
                               font = "Helvetica 13 bold",
                               pady = 5)
         
        self.labelHead.place(relwidth = 1)
        self.line = Label(self.Window,
                          width = 450,
                          bg = "#ABB2B9")
         
        self.line.place(relwidth = 1,
                        rely = 0.07,
                        relheight = 0.012)
         
        self.textCons = Text(self.Window,
                             width = 20,
                             height = 2,
                             bg = "#17202A",
                             fg = "#EAECEE",
                             font = "Helvetica 14",
                             padx = 5,
                             pady = 5)
         
        self.textCons.place(relheight = 0.745,
                            relwidth = 1,
                            rely = 0.08)
         
        self.labelBottom = Label(self.Window,
                                 bg = "#ABB2B9",
                                 height = 80)
         
        self.labelBottom.place(relwidth = 1,
                               rely = 0.825)
         
        self.entryMsg = Entry(self.labelBottom,
                              bg = "#2C3E50",
                              fg = "#EAECEE",
                              font = "Helvetica 13")
         
        # place the given widget
        # into the gui window
        self.entryMsg.place(relwidth = 0.74,
                            relheight = 0.06,
                            rely = 0.008,
                            relx = 0.011)
         
        self.entryMsg.focus()
         
        # create a Send Button
        self.buttonMsg = Button(self.labelBottom,
                                text = "Send Message",
                                font = "Helvetica 10 bold",
                                width = 20,
                                bg = "#ABB2B9",
                                command = lambda : self.sendButton(self.entryMsg.get()))

        self.buttonFile = Button(self.labelBottom,
                                text = "Send File",
                                font = "Helvetica 10 bold",
                                width = 20,
                                bg = "#ABB2B9",
                                command = lambda : self.sendButton(self.entryMsg.get()))
         
        self.buttonMsg.place(relx = 0.77,
                             rely = 0.008,
                             relheight = 0.03,
                             relwidth = 0.22)

        self.buttonFile.place(relx = 0.77, rely=0.04, relheight=0.03, relwidth=0.22)
         
        self.textCons.config(cursor = "arrow")
         
        # create a scroll bar
        scrollbar = Scrollbar(self.textCons)
         
        # place the scroll bar
        # into the gui window
        scrollbar.place(relheight = 1,
                        relx = 0.974)
         
        scrollbar.config(command = self.textCons.yview)
         
        self.textCons.config(state = DISABLED)
 
    # function to basically start the thread for sending messages
    def sendButton(self, msg):
        # print("send btn")
        self.textCons.config(state = DISABLED)
        self.packet.set_message(msg)
        self.entryMsg.delete(0, END)
        if len(msg)<2048:
            self.textCons.config(state = NORMAL)
            self.textCons.insert(END, f"You: {msg}\n\n")
            self.textCons.config(state = DISABLED)
            self.textCons.see(END)
            snd= threading.Thread(target = udp_actions.sender,args=(self.channel_name,self.udp_p1_port,self.packet))
            snd.start()
        else:
            self.textCons.config(state = NORMAL)
            self.textCons.insert(END, f"Message too long\n\n")
            self.textCons.config(state = DISABLED)
            self.textCons.see(END)
            # print("message too long")
        # snd.join()
 
    # function to receive messages
    def receive(self):
        serverPort=self.udp_p2_port
        serverSocket = socket(AF_INET, SOCK_DGRAM)
        serverSocket.bind(('', serverPort))

        print(f"Ready to receive on port {serverPort}.")

        received=None

        while True:
            status=udp_base.packet()
            status.set_username("status")
            original_packet, clientAddress = serverSocket.recvfrom(2048)
            packet=udp_base.packet().decode(original_packet)
            if packet.corrupted:
                status.ack_flag=False
            else:
                status.ack_flag=True
                if received!=packet.seq_nb:
                    self.textCons.config(state = NORMAL)
                    self.textCons.insert(END, f"{packet.get_username()}: {packet.get_message()}\n\n")
                    self.textCons.config(state = DISABLED)
                    self.textCons.see(END)
                    status.ack_nb=received=packet.seq_nb
                else:
                    status.ack_nb=received
            serverSocket.sendto(status.encode(), clientAddress)
         
    # function to send messages
    # def sendMessage(self):
    #     self.textCons.config(state=DISABLED)
    #     while True:
    #         message = (f"{self.name}: {self.msg}")
    #         client.send(message.encode(FORMAT))   
    #         break   
 
# create a GUI class object
g = GUI()