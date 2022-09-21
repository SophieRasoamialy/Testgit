
from tkinter import Radiobutton
from tkinter import X
from tkinter import Label
from tkinter import Tk
from tkinter import Frame
from tkinter import Canvas
from tkinter import Scale
from tkinter import IntVar
from tkinter import VERTICAL
import time
class feu_tri_color_v2:
    def __init__(self,fenetre):
        self.fenetre = fenetre
        
    def manuel(self):
        #manuel(1,self.fenetre)
        print("salut")
        
    def changement_couleur(self,duree_allumage):
        dessin.itemconfigure(feu_rouge, fill = "red")
        dessin.itemconfigure(feu_jaune, fill = "gray")
        dessin.itemconfigure(feu_vert, fill = "gray")
        time.sleep(duree_allumage)
        dessin.itemconfigure(feu_jaune, fill = "yellow")
        dessin.itemconfigure(feu_rouge, fill = "gray")
        dessin.itemconfigure(feu_vert, fill = "gray")
        time.sleep(duree_allumage)
        dessin.itemconfigure(feu_vert, fill = "green")
        dessin.itemconfigure(feu_rouge, fill = "gray")
        dessin.itemconfigure(feu_jaune, fill = "gray")
        time.sleep(duree_allumage)
        
    def automatique(self):
        bouton_manuel.pack_forget()
        bouton_automatique.pack_forget()
        label_rapide.pack(fill = X)
        echelle.pack(fill=X)
        label_lent.pack(fill = X)
        duree_initial = 1
        while True:
            changement_couleur(duree_initial)
        
    def change_vitesse(self,valeur_echelle):
        duree_allumage = int(valeur_echelle)
        while True:
            changement_couleur(duree_allumage)
            

if __name__ == '__main__':
    fenetre_principal  = Tk()
    variable_radio_btn = IntVar()
    variable_echelle = IntVar()
    feu_tri_color_v2 = feu_tri_color_v2(fenetre_principal)
    dessin = Canvas(fenetre_principal, width =200, height =500, bg ="ivory")
    dessin.grid(row = 0, column = 0, rowspan = 2,padx = 5, pady = 5)
    
    feu_rouge = dessin.create_oval(40,50,137,147, fill = "red")
    feu_jaune = dessin.create_oval(40,177,137,274, fill = "gray")
    feu_vert = dessin.create_oval(40,304,137,401, fill = "gray")
    
    zone_bouton = Frame(fenetre_principal, bg='#777777')
    zone_bouton.grid(row=0,column=1,ipadx=5,ipady = 5)
    
    bouton_manuel  = Radiobutton(zone_bouton, text = "Manuel", variable = variable_radio_btn, command = feu_tri_color_v2.manuel, value = 1)
    bouton_manuel.pack(fill=X)
    bouton_automatique = Radiobutton(zone_bouton, text = "Automatique", variable = variable_radio_btn, command = feu_tri_color_v2.automatique , value = 2)
    bouton_automatique.pack(fill=X)
    label_rapide = Label(zone_bouton, text = "rapide")
    label_rapide.pack_forget()
    echelle = Scale( zone_bouton, variable = variable_echelle,
           from_ = 100, to = 1,
           orient = VERTICAL)
    echelle.pack_forget()
    echelle.bind('<Button-1>', feu_tri_color_v2.change_vitesse(str(variable_echelle)))
    label_lent = Label(zone_bouton, text = "lent")
    label_lent.pack_forget()
