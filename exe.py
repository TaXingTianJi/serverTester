#!/usr/bin/env python
#coding=utf-8
import os
import threading
from time import ctime,sleep
import subprocess

process = []
counter = 2

def serverFrameworkTest(func):
    log = "testPy-%d-%d" %(counter,func)
    print log

    #p = subprocess.Popen(["./serverFrameworkTest", "-h", "127.0.0.1", "-t", "llltest", "-k", "10"])
    p = subprocess.Popen(["./serverFrameworkTest"])
    process.append(p)
    print "process.append %d" %(func)

threads = []

for i in range(1,counter):
    print "start"
    t = threading.Thread(target=serverFrameworkTest,args=(i,))
    threads.append(t)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    sleep(0.01)

    raw_input('q')

    for sub in process:
        print sub.pid
        a =sub.kill()
    # if (a!= None):
    #     print a

    print "all over %s" %ctime()