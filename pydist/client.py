import socket
import thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 11000))

m = s.recv(10)
m = int(m)

s.send(str(sum(range(m, m + 10))))


s.close()
