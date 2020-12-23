import socket
import sys
from threading import Thread
host ='192.168.43.59'
port= 46000
BUFFER_SIZE = 1024


class client(Thread):
    def __init__(self,conn):
        Thread.__init__(self)
        self.communication=conn

    def run(self):
        nom=self.getName()
        while 1:
            msgClient=self.communication.recv(1024).decode("UTF8")
            if not msgClient or msgClient.upper()=="FIN":
                break
            message="%s>%s"%(nom,msgClient)
            print(message)
            for cle in conn_client:
                if cle!=nom:
                    conn_client[cle].send(message.encode("UTF8"))

        self.communication.close()
        del conn_client[nom]
        print("Client %s deconnecté."%nom)

mySocket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    mySocket.bind((host,port))
except socket.error:
    print("La liaison du socket à l'adresse choisie a échoué.")
    sys.exit()

# configure la socket en sock. serveur TCP
mySocket.listen(5)

conn_client={}
while 1:
    print("Serveur prêt, en attente de client ...")
    communication,adresse=mySocket.accept()
    th=client(communication)
    th.start()
    it=th.getName()
    conn_client[it]=communication
    print("client %s connecté, adresse IP %s,port %s." %\
          (it,adresse[0],adresse[1]))
    #msg="Vous êtes connecté,Envoyé vos messages."
    #communication.send(msg.encode('UTF8'))
                    
