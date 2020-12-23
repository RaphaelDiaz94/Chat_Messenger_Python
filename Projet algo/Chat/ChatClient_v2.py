from threading import Thread
import ChatVue_v1 as CV

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
        
    def __init__(self,conn,vt):
        Thread.__init__(self)
        self.connexion=conn
        self.vt = vt
        
    def run(self):
        r=1
        while r==1:
            r=0
            message_emis=self.vt
            self.text.insert('end',"Greg : " + message_emis.get() + "" + "\n")
            self.connexion.send(message_emis.get().encode("UTF8"))
            
            

            

