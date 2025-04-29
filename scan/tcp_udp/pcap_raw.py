from time import time
from struct import pack
import socket
from tempfile import NamedTemporaryFile

class PCAPCreator:
    def __init__(self) -> None:
        self.tmp = NamedTemporaryFile('wb', suffix='.pcap', delete=False)
        self.__header()
    
    def __header(self):
        self.tmp.file.write(pack('<I2Hi3I', 0xa1b2c3d4, 2, 4, 0, 0, 65535, 1))
        
    def blob(self, data):
        self.tmp.file.write(pack('<4I', int(time()), 0, len(data), len(data)))
        self.tmp.file.write(data)
        
    def close(self):
        print(self.tmp.name)
        self.tmp.file.close()


class Sniff:
    def __init__(self, iface) -> None:
        self.iface = iface
        self.pcap = PCAPCreator()
        self.sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 212992)
        self.sock.bind((self.iface, 3))
        
    def recv(self):
        #while True:
        data, dump = self.sock.recvfrom(1500)
        self.pcap.blob(data)

def main():            
    sn = Sniff('lo')
    i = 0
    while True:
        i += 1
        if i <= 100:
            sn.recv()
        if i == 100:
            sn.pcap.close()
            return False
    
if __name__ == '__main__':
    main()