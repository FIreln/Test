from socket import *

host = 'localhost'
port = 8000
bufsiz = 1024
addr = (host,port)


cs = socket(AF_INET,SOCK_STREAM)
cs.connect(addr)
while True:
    data = input('> ')
    if not data:
        break
    cs.send(data)
    data = cs.recv(bufsiz)
    if not data:
        break
    print(data.decode('utf-8'))
cs.clock()
