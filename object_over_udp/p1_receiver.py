import base
import actions
import threading

peer1_port=12001
peer2_port=12002

channel_name="127.0.0.1"

actions.receiver(peer1_port)