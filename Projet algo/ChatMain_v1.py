"""
IPSA Projet Chat : MAIN
"""

import ChatClient_v2 as CC
import ChatVue_v1 as CV
import socket
import sys

def envoi(e):
    global CV
    CV.console.insert('end',CV.var_texte.get())


if __name__ == "__main__":
    print("lets go")
    host = "192.168.43.59"
    port = 46000
    #------------------------- Connection au socket ------------------

    connexion=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        connexion.connect((host,port))
    except socket.error:
        print("la connexion a echoue")
        sys.exit()
    print("connexion etablie avec le serveur")



    #------------------------- Creation des threads ------------------

    th_E=CC.emission(connexion)
    th_R=CC.reception(connexion)
    th_R.text=CV.console
    th_E.text=CV.console
    CV.fenetre.bind('<Return>',envoi)
    
    th_E.start()
    th_R.start()
    CV.fenetre.mainloop()


    #------------------------- Destruction des threads et de la fenetre ------------------

    print("attente de fin des threads")
    th_E.join()
    print("attente de fin du dernier threads")
    th_R.join()
    print("plus rien a faire...")
    fenetre.destroy()
