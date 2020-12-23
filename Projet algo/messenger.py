import socket
import sys
from threading import Thread
host='192.168.43.77'
port = 46000
BUFFER_SIZE = 1024


class reception(Thread) :
    
    def __init__(self,conn):
        
        Thread.__init__(self)
        self.connexion=conn
        
   
    def run(self) :
      
        while 1:
            message_recu=self.connexion.recv(1024).decode("ascii")
            print("message recu : ", message_recu)
            if message_recu and message_recu.upper()!=("fin" or "FIN"):
                break
            th_E._stop()
            print("client arrete, connexion interrompue")
            self.connexion.close()

  
class emission(Thread):
        
    def __init__(self,conn):
        Thread.__init__(self)
        self.connexion=conn
        
    def run(self):
        while 1:
            message_emis=input()
            self.connexion.send(message_emis.encode("ascii"))
            
    

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
          
        

