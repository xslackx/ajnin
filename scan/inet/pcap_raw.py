from time import time
from struct import pack
from tempfile import NamedTemporaryFile

class PCAPCreator:
    def __init__(self, to_delete: bool) -> None:
        self.tmp = NamedTemporaryFile('wb', suffix='.pcap', delete=to_delete)
        self.__header()
    
    def __header(self):
        self.tmp.file.write(pack('<I2Hi3I', 0xa1b2c3d4, 2, 4, 0, 0, 65535, 1))
        
    def blob(self, data):
        self.tmp.file.write(pack('<4I', int(time()), 0, len(data), len(data)))
        self.tmp.file.write(data)
        
    def close(self):
        print(self.tmp.name)
        self.tmp.file.close()