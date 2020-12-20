import socket
import sys


c= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

host =sys.argv[1]
port = 69
buf =1024
addr = (host,port)

file_name=sys.argv[2]


c.sendto(file_name.encode(),addr)

f=open(file_name,"rb")
data = f.read(buf)
while (data):
    if(c.sendto(data,addr)):
        print ("sedang di muat turun ...")
        data = f.read(buf)
   
c.close()
f.close()



#msg="Hello UDP Server"
#c.sendto(msg.encode("utf-8"),('192.168.43.3',12345))
#data,addr=c.recvfrom(4096)
#print("Server Says")
#print(str(data))
#c.close()
