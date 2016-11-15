#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 1202                # Reserve a port for your service.
print("Connecting at server at port: %i with the host: %s" % (port,host))

try:
    s.connect((host, port))
except ValueError:
    print("Could not connect to server")
print("Server: ", s.recv(1024))
s.close                     # Close the socket when done
