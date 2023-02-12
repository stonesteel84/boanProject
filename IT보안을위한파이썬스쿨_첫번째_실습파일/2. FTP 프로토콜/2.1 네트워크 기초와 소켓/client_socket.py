import socket

with socket.socket() as s :
    addr = ("www.daum.net",80) #443 web
    s.connect(addr) # 전화 걸기
    s.send("GET /\n".encode()) # 데이터 보내기 : 웹 요청
    data = s.recv(1024) # 1024바이트 데이터 받기
    print(data.decode())
