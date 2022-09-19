import os
import sys
from socket import * #imports all from socket
from threading import * #imports all from threads
inp = sys.argv[1:] #argumentative input for command line inputs -p, -h 
def res(): #function for printing service names of ports if found
    if (len(main_array) == 0):
        print("No TCP Ports are open in given range")
        sys.exit()
    print("Port\tService")
    for p in main_array:
        try:
            serv = getservbyport(p)
        except:
            serv = "unknown service name"
        print(str(p)+"\t"+serv)
try:
    if not(inp[0]== '-p' and inp[3] == '-h'):
        raise error
    port_start = int(inp[1])
    port_stop = int(inp[2])
    ip = inp[4]
    if(port_start > port_stop): #starting port value should not be larger than the port value where it stops
        raise error
except:
    print("Usage, PS Port Ranges have to be separated by spaces, as when I would separate by hyphens it would not compile at all: \n python ""portscan.py"" -p <port-start> <port_stop> -h <ip>")
    sys.exit()
main_array = []
thread_array = []
setdefaulttimeout(0.01)
lock = Lock()
def connection(ipx, portx,lock):
    addr = (ipx,portx)
    sock = socket(AF_INET, SOCK_STREAM)
    result = sock.connect_ex(addr)
    sock.close()
    lock.acquire()
    if (result == 0):
        main_array.append(portx)
    lock.release()
for port in range(port_start,port_stop+1):
    t = Thread(target = connection, args = (ip, port,lock)) #create a new thread
    t.start()
    thread_array.append(t)
for thread in thread_array:
    thread.join()
    
print("-"*50)
print ("Portscan Complete!")
res()#function for printing service names of ports if fou