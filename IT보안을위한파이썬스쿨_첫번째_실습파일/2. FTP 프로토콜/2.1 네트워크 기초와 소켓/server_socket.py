import socket

with socket.socket() as s :
    addr = ("0.0.0.0",80) # 80번으로 개통하겠다.
    s.bind(addr)
    s.listen()
    print("start server..")
    
    conn, addr = s.accept() # 전화수락
    print("accept {}:{}".format(addr[0],addr[1]))
    data = conn.recv(1024)
    conn.send("Hi This is Web".encode())
