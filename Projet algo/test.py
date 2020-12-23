
import tkinter as tk
 
 
#Une fonction très simpliste pour l'exemple
def print_name(event):
    .insert('end', value)
 
 
fenetre = tk.Tk()
value = tk.StringVar(fenetre)
value.set("texte par défaut")
 
entree = tk.Entry(fenetre, textvariable=value, width=30)
entree.pack()
 
#On lie la fonction à l'Entry
#La fonction sera exécutée à chaque fois que l'utilisateur appuie sur "Entrée"
entree.bind("<Return>", print_name)
 
 
fenetre.mainloop()
