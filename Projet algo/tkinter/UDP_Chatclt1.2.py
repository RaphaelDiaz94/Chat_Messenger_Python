#!/usr/bin/env python
""" Simple UDP chat user with threads
    utilisation : UDP_Chatclt1.py ip_locale port_local ip_distante port_distant
    IPSA IN321 2018-2019
"""

import socket
import threading

import sys          # for getting command line args and read stdin while tkinter running
import binascii     # for generating hex representation of raw data
import time         # to display time
import tkinter      # to diplay a text window

MAXREAD = 256    # taille d'une lecture dans une socket (en octets)

def echo_udp_on(ip,port,console):
    # 1 # création d'une socket
    sock = socket.socket(socket.AF_INET, # osi nv 3 : internet
                     socket.SOCK_DGRAM)  # osi nv 4 : udp
    # 2 # association à une ip locale et un port local
    sock.bind((ip,port))

    # 3 # boucle de lecture et affichage de la socket
    msg = 'vide'
    while msg != 'fin':
        # 3.1 lecture de la socket
        data, addr = sock.recvfrom(MAXREAD)
        # 3.2 transformation des octets en type string
        msg = data.decode('utf-8')
        # 3.3 transformation des octets en hexa en type string 
        s = '0x'+''.join(str(hex(b))[2:] for b in data)
        # 3.4 affichage
        print(time.strftime("%H:%M"),addr,':',msg,s)
        console.insert(tkinter.END,time.strftime("%H:%M")+' [autre]:'+msg+"\n")

    print("end of recv thread")

def write_udp_to(ip,port,console):
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    msg = "vide"
    while msg != 'fin':
        #msg = input("toi:")   # causes pb with tkinter, replaced with sys.stdin.readline
        #print("toi:",end='',flush=True)
        msg = sys.stdin.readline()[:-1]
        console.insert(tkinter.END,time.strftime("%H:%M")+' [toi]  :'+msg+"\n")
        data = msg.encode('utf-8')
        if len(data) > MAXREAD :
            print("toi:",data[:MAXREAD].decode("utf-8"))
            sock.sendto(data[:MAXREAD], (ip,port))
        else : 
            sock.sendto(msg.encode('utf-8'), (ip,port))
        time.sleep(0.5)
    console.master.quit()

    print("end of send thread")

def main(argv):
    # 1 init addrs and ports
    LOCAL_IP = "127.0.0.1"      # 0.0.0.0 is all local interfaces
    LOCAL_PORT = 3003
    TRG_IP = "127.0.0.1"        # 255.255.255.255 is broadcast addr
    TRG_PORT = 3003

    # 2 verify if args are provided through command line
    if len(argv) >= 5:
        LOCAL_IP = sys.argv[1]
        LOCAL_PORT = int(sys.argv[2])
        TRG_IP = sys.argv[3]
        TRG_PORT = int(sys.argv[4])

    # 3 display operating parameters
    print(LOCAL_IP,"reçoit sur",LOCAL_PORT,"(moi)")
    print(TRG_IP  ,"reçoit sur",TRG_PORT,"(l'autre)")

    # 4 init a display console
    fenetre = tkinter.Tk()
    console = tkinter.Text(fenetre)
    console.pack()

    # 6 launch threads
    t = []
    try:
       t.append(threading.Thread( target=echo_udp_on,args= (LOCAL_IP, LOCAL_PORT,console, ) ))
       t.append(threading.Thread( target=write_udp_to, args=(TRG_IP,TRG_PORT,console, ) ))
       for th in t :
           th.start()
    except BaseException as e:
       print ("Error: unable to start thread")
       print(e)
       #raise
    fenetre.mainloop()

    print("wainting for end....")
    # 6 wait end of threads
    for th in t :
        th.join()
        print("one thread finished")
    fenetre.destroy()
    

if __name__ == "__main__":
    print("----début----")
    main(sys.argv)
    print("----fin----")

