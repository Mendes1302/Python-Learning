import socket


HOST = '192.168.2.50'    
PORT = 12500            

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

tcp.sendall(b'Lucas Mendes Barbosa')
data = tcp.recv(1024)
print(data)