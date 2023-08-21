
import socket
import sys
from datetime import datetime
from timeit import default_timer

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("invalid amount of arguments")
    print ("syntax is : soc.py <ip>")


try:
    for port in range(1,65365):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result=s.connect_ex((target,port))
        if result == 0:
            print( 'port %s is open'%(port))


except KeyboardInterrupt:
    print ('exiting program')
    sys.exit()

except socket.error:
    print ('Cannot connect to port')
    sys.exit()











