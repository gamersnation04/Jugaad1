import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 25))
server.listen(1)

print('Server listening on port 25...')

while True:
    conn, addr = server.accept()
    print('Connection from:', addr)

    sum_result = 0
    while True:
        data = conn.recv(1024).decode('utf-8')
        if data == 'stop':
            break
        sum_result += int(data)

    conn.send(str(sum_result).encode('utf-8'))
    conn.close()
    print('Connection Closed.')

server.close()




#First  run the server file from cmd and then run the client file on another cmd tab.
'''

In case if external asked for the String to send to server. use this code
import socket
import random
s = socket.socket() # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345 # Reserve a port for your service.
s = socket.socket()
s.bind((host, port)) # Bind to the port
s.listen(5) # Now wait for client connection.
conn, addr = s.accept()
print('Got connection from ', addr[0], '(', addr[1], ')')
while True:
    data = conn.recv(1024)
    print(data.decode("utf-8"))
    if not data:
        break
    conn.sendall(data)

conn.close()
print('Thank you for connecting')
'''