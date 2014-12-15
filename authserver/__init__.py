import socket

s = socket.socket()   
s.bind((socket.gethostname(), 5000))  
s.listen(1)  
  
sc, addr = s.accept()  
  
while True:  
    recibido = sc.recv(1024)  
    if recibido == "quit":  
        break        
    print "Recibido:", recibido  
    sc.send(recibido)  
  
print "adios"  
  
sc.close()  
s.close() 