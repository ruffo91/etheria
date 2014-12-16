import socket
import threading

tLock = threading.Lock()

host = "127.0.0.1"
port = 0

server = ("127.0.0.1", 5000)

shutdown = False

def receving(name, sock):
    while not shutdown:
        try:
            tLock.acquire()
            while True:
                data = sock.recvfrom(1024)
                print str(data)
        except:
            pass
        finally:
            tLock.release()
            
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("127.0.0.1", 5000))
s.setblocking(0)

rT = threading.Thread(target = receving, args = ("RecvThread", s))
rT.start()

alias = raw_input("Nombre: ")
message = raw_input(alias + "-> ")
while message != "q":
    if message != "":
        s.send(alias + ": " + message)
    message = raw_input(alias + "-> ")
    
shitdown = True
rT.join()
s.close()