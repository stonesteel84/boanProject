import socket
import threading

def recv_data():
    with socket.socket() as s:
        s.bind(("0.0.0.0",96 * 256 + 105))
        s.listen()
        print("start data server:", 96 * 256 + 105)
        conn, addr = s.accept()
        #s.connect((ip,24032))
        print("client = {}: {}".format(
            addr[0],addr[1]))
        #print(addr)
        #s.connect(addr)
        #s.send("TEST".encode())
        return (s.recv(1024).decode())

with socket.socket() as s:
    ip = "172.30.1.11"
    addr = (ip,21)
    s.connect(addr)
    print(s.recv(1024).decode())
    s.send("USER anonymous".encode())
    print(s.recv(1024).decode())
    s.send("PASS anonymous".encode())
    print(s.recv(1024).decode())
    s.send("PWD".encode())
    print(s.recv(1024).decode())
    s.send("PORT 170,30,1,1,96,105".encode()) # p1*256+p2 = 4*256 + 15
    print(s.recv(1024).decode())
    
    
    t = threading.Thread(target=recv_data)
    t.start()

    print("a")
    s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 0)
    s.send("LIST\r\n".encode())
    print(s.recv(1024).decode())
    #
