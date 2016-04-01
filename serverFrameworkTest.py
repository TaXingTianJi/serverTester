#server framework tester
import socket
import time
import struct

header = '0x05'
cmd = 1002
length = 3
data = 'abc'

string = struct.pack('!HHs',cmd,length,data)

#address = ('127.0.0.1',4150)
address = ('127.0.0.1',8888)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

s.send('  V2') 	#protocol v1

while 1:
  #s.send('\ncmd len data\n cmd1 len1 data1\n cmd2 len2 data2\n')
  #t0 = time.clock()
  t0 = time.time()
  #s.send('\n a b c')
  s.send(string)
  time.sleep(10.1)

  data = s.recv(1024)
  if not data:
    break
  print data
  #print "ping %d" %(time.clock() - t0)
  print "ping %d %s" %(time.time()*1000 - t0*1000,'ms')
 

s.close()
