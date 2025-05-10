import struct
from os.path import exists

class CM:
    def __init__(self, directory: str) -> None:
        self.dir = directory
        self.message_pack = []

    def load_services(self, file: str):
        self.file = file
        self.fullpath = self.dir + "/" + self.file
        if exists(self.fullpath):
            with open(self.fullpath, 'r') as service:
                return service.read()

    def struct_message(self, service: str):
        self.services = service.split('\n')
        
        for details in self.services:
            item = details.split(",")
            self.message_pack.append(
                struct.pack("<iss", int(item[0]), str(item[1]).encode(), str(item[2]).encode() ) 
                )
