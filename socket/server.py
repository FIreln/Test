from socket import *
from time import ctime

host = '192.168.1.105'
port = 8000
bufsiz = 1024
addr = (host,port)


ss = socket(AF_INET,SOCK_STREAM)
ss.bind(addr)
ss.listen(5)

while True:
    print('wating for connecting....')
    cs , addr = ss.accept()
    print('...connect from;',addr)
    while True:
       data = cs.recv(bufsiz)
       if not data:
           break
       ss.send('[%s] %s' % (ctime(),data))
    cs.clock()
ss.clock()
