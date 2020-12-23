"""
IPSA Projet Chat: vue
"""
import tkinter as tk

fenetre=tk.Tk()
console=tk.Text(fenetre)
console.pack()

var_texte = tk.StringVar()
ligne_texte = tk.Entry(fenetre, textvariable=var_texte, width=30)
ligne_texte.pack()

if __name__ == "__main__":
    #controler part...just for testing...
    fenetre.bind('<Return>',lambda e : console.insert('end',var_texte.get()))
