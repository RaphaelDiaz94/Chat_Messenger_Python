import socket
import sys
from threading import Thread
host='192.168.43.59'
port = 46000
BUFFER_SIZE = 1024


class reception(Thread) :
    
    def __init__(self,conn):
        Thread.__init__(self)
        self.connexion=conn
        
   
    def run(self) :
        while "fabien":
            message_recu=self.connexion.recv(1024).decode('UTF8')
            print("message recu : ", message_recu)
            if message_recu.upper() == "FIN":
                print("client arrete, connexion interrompue")
                self.connexion.close()
                th_E._stop()
                break
            
  
class emission(Thread):
        
    def __init__(self,conn):
        Thread.__init__(self)
        self.connexion=conn
        
    def run(self):
        while 1:
            message_emis=input()
            self.connexion.send(message_emis.encode('UTF8'))
            
    

connexion=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    connexion.connect((host,port))
except socket.error:
    print("la connexion a echoue")
    sys.exit()
print("connexion etablie avec le serveur")

th_E=emission(connexion)
th_R=reception(connexion)
th_E.start()
th_R.start()
print("attente de fin des threah")
th_E.join()
print("attente de fin du dernier thread threah")
th_R.join()

print("plus rien a faire...")

        

