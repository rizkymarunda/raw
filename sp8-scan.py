#!/opt/anaconda3/bin/python
import socket
ip = raw_input("Target IP : ")
port = input("Target Port : ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if s.connect_ex((ip, port)):
   print "Port", port, "is closed"
else:
   print "Port", port, "is open"

