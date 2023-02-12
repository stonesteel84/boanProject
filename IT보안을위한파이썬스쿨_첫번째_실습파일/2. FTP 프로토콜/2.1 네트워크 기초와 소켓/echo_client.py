import socket

addr = ("127.0.0.1", 4444)


with socket.socket() as s:
    s.connect(addr)
    
    while(1):
        str1 = input("echo: ").encode()
        s.send(str1)
        data = s.recv(1024)
        print(data.decode())
