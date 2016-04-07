#server framework tester
import socket
import time
import struct

header = 0x05	# 1 byte
cmd = 1002	    # 4 byte
length = 3	    # 4 bytexz
data = 'abc'	# len byte

string = struct.pack('!b2i3s',header,cmd,length,data)

# send of piece
str1 = struct.pack('!b2i',header,cmd,length)
str2 = struct.pack('!3s',data)

#address = ('127.0.0.1',4150)
address = ('127.0.0.1',8888)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

s.send('  V1') 	#protocol v1

while 1:
  t0 = time.time()
  #s.send('\nabc')

  s.send(string)
  time.sleep(2)
  s.send(str1)
  time.sleep(2)
  s.send(str2)

  data = s.recv(1024)
  if not data:
    break
  print data
  print "ping %d %s" %(time.time()*1000 - t0*1000,'ms')


s.close()
