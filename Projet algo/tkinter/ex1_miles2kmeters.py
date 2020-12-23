""" IPSA IN14 2016
    TP11 : IHM
    exmple 1 : convertion

"""

import tkinter as tk
from tkinter import ttk

programme = tk.Tk()
programme.title("Miles en kilometres")
miles = tk.StringVar()
kmetres = tk.StringVar()

def convertir(*args):
    kmetres.set(float(miles.get()) * 1.609)

fenetre = ttk.Frame(programme, padding="3 3 12 12")
fenetre.grid(column=0, row=0)

Entrée = ttk.Entry(fenetre, width=7, textvariable=miles)
Texte1 = ttk.Label(fenetre, text="miles")
Entrée.grid(column=2, row=1)
Texte1.grid(column=3, row=1)

ttk.Label(fenetre, text="équivaut à"   ).grid(column=1, row=2)
ttk.Label(fenetre, textvariable=kmetres).grid(column=2, row=2)
ttk.Label(fenetre, text="kilometres"   ).grid(column=3, row=2)

ttk.Button(fenetre, text="(convertir)", command=convertir).grid(column=3, row=3)
programme.bind('<Return>', convertir)       # lien controleur: touche - action

programme.mainloop()

""" related doc

    Label
    http://effbot.org/tkinterbook/label.htm
    http://tmml.sourceforge.net/doc/tk/label.html
"""
