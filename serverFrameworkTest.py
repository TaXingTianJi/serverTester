#server framework tester
import socket
import time

address = ('127.0.0.1',4150)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

s.send('  V2') 	#protocol v1

while 1:
  #s.send('\ncmd len data\n cmd1 len1 data1\n cmd2 len2 data2\n')
  #t0 = time.clock()
  t0 = time.time()
  s.send('\n IDENTIFY ')
  time.sleep(0.1)

  data = s.recv(1024)
  if not data:
    break
  print data
  #print "ping %d" %(time.clock() - t0)
  print "ping %d %s" %(time.time()*1000 - t0*1000,'ms')
 

s.close()
