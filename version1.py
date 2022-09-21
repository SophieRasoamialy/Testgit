from tkinter import Canvas
from tkinter import Tk
from tkinter import Button
from tkinter import X
from tkinter import Frame
from tkinter import messagebox
class feu_tri_color:
    def __init__(self,position_feu,fenetre_principal):
        self.position_feu = position_feu
        self.fenetre_principal = fenetre_principal
    def suivant(self):
        if(self.position_feu == 1):
            dessin.itemconfigure(feu_rouge, fill = "gray")
            dessin.itemconfigure(feu_jaune, fill = "yellow")
            self.position_feu  = 2
        elif(self.position_feu == 2):
            dessin.itemconfigure(feu_vert, fill = "green")
            dessin.itemconfigure(feu_jaune, fill = "gray")
            self.position_feu  = 3
        elif(self.position_feu == 3):
            dessin.itemconfigure(feu_rouge, fill = "red")
            dessin.itemconfigure(feu_vert, fill ="gray")
            self.position_feu  = 1

    def initialiser(self):
        
        dessin.itemconfigure(feu_rouge, fill = "red")
        dessin.itemconfigure(feu_vert, fill = "gray")
        dessin.itemconfigure(feu_jaune, fill = "gray")
        self.position_feu = 1
        
    def confirm(self):
        reponse = messagebox.askyesnocancel("Question", "Voulez-vous continuer ?")
        if(reponse == True):
            self.fenetre_principal.destroy()
            
if __name__ == '__main__':
    fenetre_principal = Tk()
    position_feu_init = 1
    feu_tri_color = feu_tri_color(position_feu_init,fenetre_principal)
    dessin = Canvas(fenetre_principal, width =200, height =500, bg ="ivory")
    dessin.grid(row = 0, column = 0, rowspan = 2,padx = 5, pady = 5)
    
    feu_rouge = dessin.create_oval(40,50,137,147, fill = "red")
    feu_jaune = dessin.create_oval(40,177,137,274, fill = "gray")
    feu_vert = dessin.create_oval(40,304,137,401, fill = "gray")
    zone_bouton = Frame(fenetre_principal, bg='#777777')
    zone_bouton.grid(row=0,column=1,ipadx=1,ipady = 5)

    bouton_suivant  = Button(zone_bouton, text = "Suivant", command = feu_tri_color.suivant)
    bouton_suivant.pack(fill=X)
    bouton_initialiser = Button(zone_bouton, text = "Initialiser", command = feu_tri_color.initialiser)
    bouton_initialiser.pack(fill=X)
    bouton_quitter = Button(zone_bouton, text = "Quitter", command = feu_tri_color.confirm)
    bouton_quitter.pack(fill=X)
