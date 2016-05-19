# server framework tester
import socket
import time
import struct

delta = 0.0  # sleep time

# header = 0x05	# 1 byte
# cmd = 1002	    # 4 byte
# length = 3	    # 4 byte
# data = 'abc'	# len byte
#
# # string = struct.pack('!b2i3s',header,cmd,length,data)
# string = struct.pack('!b2i3sb2i3s',header,cmd,length,data,header,cmd,length,data)

# # send of piece
# str1 = struct.pack('!b',header)
# str2 = struct.pack('!i',cmd)
# str3 = struct.pack('!i',length)
# str4 = struct.pack('!3s',data)

address = ('127.0.0.1', 60060)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

# s.send('  V1') 	#protocol v1
s.send(' ')  # protocol v1
print "send 1byte"
# time.sleep(1)

s.send(' ')  # protocol v1
print "send 1byte"
# time.sleep(1)

s.send('V')  # protocol v1
print "send V"
# time.sleep(1)

s.send('1')  # protocol v1
print "send 1"
# time.sleep(1)

start = time.time()
packs = 0
err = 0
suc = 0
testTime = 5  # min

while 1:
    t0 = time.time()

    header = 0x05  # 1 byte
    cmd = 10011  # 4 byte
    data = time.ctime()
    length = len(data)  # 4 byte

    string = struct.pack('!b2i24s', header, cmd, length, data)
    # print "cmd->[%d] len->[%d] data->[%s] str->[%s]\n" %(cmd,length,data,string)
    # complete pack
    time.sleep(delta)
    s.send(string)
    # s.send(str1)
    # time.sleep(delta)
    # s.send(str2)
    # time.sleep(delta)
    # s.send(str3)
    # time.sleep(delta)
    # s.send(str4)
    print "send one packet"
    packs += 1

    #  time.sleep(10)
    # split pack
    # time.sleep(2)
    # s.send(str1)
    # time.sleep(2)
    # s.send(str2)

    data = s.recv(1024)
    if not data:
        break
    print '%s%s' % (data, '\n')
    if "error" in data:
        err += 1
    if "succ" in data:
        suc += 1

    print "ping %d %s" % (time.time() * 1000 - t0 * 1000, 'ms')

    if time.time() * 1000 - start * 1000 >= testTime * 60 * 1000:
        print "60s\n"
        break

s.close()
end = time.time()
print "totalPack->%d time->%dms, err->%d suc->%d avgPing->%dms qps->%d" \
      % (packs, end * 1000 - start * 1000, err, suc, (end * 1000 - start * 1000) / (err + suc), suc / (testTime * 60))
