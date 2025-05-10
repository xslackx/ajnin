from .pcap_raw import PCAPCreator
from time import time
import socket
class Sniff:
    def __init__(self, iface) -> None:
        self.iface = iface
        self.pcap = PCAPCreator()
        self.sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 212992)
        self.sock.bind((self.iface, 3))
        
    def recv(self):
        data, dump = self.sock.recvfrom(1500)
        self.pcap.blob(data)
