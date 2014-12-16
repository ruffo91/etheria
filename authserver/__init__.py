import socket
import time


host = "127.0.0.1"
port = 5000

clientes = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

salir = False

print "Servidor Iniciado"

while not salir:
    try:
        data, addr = s.recvfrom(1024)
        
        if "Salir" in str(data):
            salir = True
        if addr not in clientes:
            clientes.append(addr)
            
        print time.ctime(time.time()) + str(addr) + ": :" + str(data)
        
        for cliente in clientes:
            s.sendto(data, cliente)
            
    except:
        pass
    
s.close()

