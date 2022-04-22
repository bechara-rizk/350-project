THE FILE-SENDING FEATURE USES 3 PYTHON FILES:

I)    actions.py : contains the file_sender() and file_receiver() functions ; these are the core of the code.

These functions will be given 2 arguments: receiverName: corresponds to the receiver host IP address 
                                           receiverPort: corresponds to the receiving port number
                                           
II)   peer1.py and peer2.py: use threading to run the functions of (imported) actions.py simultaneously.
      Each peer corresponds to a host, and both hosts can send and receive files in the same time, to/from the same port.
 
peer1.py and peer2.py should be run simultaneously to create a TCP connection prior to sending files; you don't have to run actions.py for the feature to work.
      
For this feature to be useful, the file should exist in the same directory as the python files.
