from socket import (
    socket, 
    AF_INET, 
    AF_INET6, 
    SOCK_STREAM,
    SOCK_DGRAM)

    
def socket_scan(host: tuple, options: dict, timeout=60):
    for option in options.items():
        if option[1] == True and option[0] == "inet6": pass
        if option[1] == True and option[0] == "inet":
            sock = socket(AF_INET, SOCK_STREAM) if options.get("stream") else None
            if sock:
                if sock.connect_ex(host) == 0:
                    print(sock.dup())
                    print(sock.getpeername())
                                        
                    return True
            else: 
                return False


host=("localhost", 443)

options = {
    "inet6": True,
    "inet": True,
    "stream": True,
    "dgram": False
}
