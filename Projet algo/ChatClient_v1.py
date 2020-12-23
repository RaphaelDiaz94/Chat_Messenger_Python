from tkinter import *
import socket
import sys
from threading import Thread
from time import *
host='192.168.43.59'
port = 46000

#------------------------- Classe reception ------------------

class reception(Thread) :
    
    def __init__(self,conn):
        Thread.__init__(self)
        self.connexion=conn
        self.text = None
        
   
    def run(self) :
        while True :
            message_recu=self.connexion.recv(1024).decode('UTF8')
            print("*"+message_recu+"*")
            self.text.insert('end',"recu" + message_recu + "" + "\n")
            if message_recu.upper() == "FIN":
                print("client arrete, connexion interrompue")
                self.connexion.close()
                th_E._stop()
                break

#------------------------- Classe emission ------------------
            
class emission(Thread):
        
    def __init__(self,conn):
        Thread.__init__(self)
        self.connexion=conn
        
    def run(self):
        while 1:
            message_emis=input()
            self.text.insert('end',"Greg : " + message_emis + "" + "\n")
            self.connexion.send(message_emis.encode('UTF8'))

#------------------------- Creation de la fenetre graphique ------------------
            
fenetre = Tk()
fenetre.geometry("300x230")
console = Text(fenetre)
console.pack()

cadre = Frame(fenetre, width = 100, height = 50, borderwidth = 1)
cadre.pack(fill=BOTH)
message = Label(cadre, text="notre fenetre")
message.pack(side="top",fill="x")
#------------------------- Connection au socket ------------------

connexion=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    connexion.connect((host,port))
except socket.error:
    print("la connexion a echoue")
    sys.exit()
print("connexion etablie avec le serveur")



#------------------------- Creation des threads ------------------

th_E=emission(connexion)
th_R=reception(connexion)
th_R.text=console
th_E.text=console
th_E.start()
th_R.start()
fenetre.mainloop()


#------------------------- Destruction des threads et de la fenetre ------------------

print("attente de fin des threads")
th_E.join()
print("attente de fin du dernier threads")
th_R.join()
print("plus rien a faire...")
fenetre.destroy()
