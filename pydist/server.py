import socket
import thread

class Result(object):
	pass

def client_thread(clientsocket, address, start, result):
	print str(address) + " connected"

	clientsocket.send(str(start))

	m = int(clientsocket.recv(10))
	result.r = m

	clientsocket.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 11000))

s.listen(5)

start = 0
threads = []
while 1:
	(clientsocket, address) = s.accept()
	threads.append(Result())
	thread.start_new_thread(client_thread, (clientsocket, address, start, threads[-1]))
	start = start + 10
	
	if start > 50:
		for result in threads:
			print result.r
		break

