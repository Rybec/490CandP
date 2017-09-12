import threading

def func(l):
	for i in xrange(len(l)):
		l[i] = l[i] * 2

li = range(20)
li0 = li[0:10]
li1 = li[10:]
t0 = threading.Thread(target=func, args=(li0,))
t1 = threading.Thread(target=func, args=(li1,))

t0.start()
t1.start()
print "Threads started"
t0.join()
t1.join()

li = li0 + li1
print li
