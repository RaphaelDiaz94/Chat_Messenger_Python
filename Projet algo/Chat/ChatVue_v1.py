"""
IPSA Projet Chat: vue
"""
import tkinter as tk
import ChatClient_v2 as CC

fenetre=tk.Tk()
console=tk.Text(fenetre)
console.place(x=300, y=100, width=700, height=400)
console.config(bg="sky blue")


var_texte = tk.StringVar()
ligne_texte = tk.Entry(fenetre, textvariable=var_texte, width=30)
ligne_texte.place(x=500, y=520, width=300, height=30)
fenetre.bind('<Return>',lambda e : console.insert('end',var_texte.get()))


cadre=tk.Frame(fenetre)
cadre.place(x=500,y=40,width=300, height=30)
bienvenue=tk.Label(cadre,text="Bievenue sur la Messagerie IPSA-TALK")
bienvenue.pack()
bienvenue.config(bg='blue', fg='yellow')

if __name__ == "__main__":
    #controler part...just for testing...
    fenetre.bind('<Return>',lambda e : console.insert('end',var_texte.get()))
