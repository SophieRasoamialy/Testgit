from tkinter import *
from tkinter import messagebox
class manuel:
    def __init__(self,i,fenetre):
        self.i = 1
        self.fenetre = fenetre
    def suivant(self):
        if(self.i == 1):
            dessin.itemconfigure(rouge, fill = "gray")
            dessin.itemconfigure(jaune, fill = "yellow")
            self.i  = 2
        elif(self.i == 2):
            dessin.itemconfigure(vert, fill = "green")
            dessin.itemconfigure(jaune, fill = "gray")
            self.i  = 3
        elif(self.i == 3):
            dessin.itemconfigure(rouge, fill = "red")
            dessin.itemconfigure(vert, fill ="gray")
            self.i  = 1

    def initialiser(self):
        
        dessin.itemconfigure(rouge, fill = "red")
        dessin.itemconfigure(vert, fill = "gray")
        dessin.itemconfigure(jaune, fill = "gray")
        self.i = 1
        
    def confirm(self):
        reponse = messagebox.askyesnocancel("Question", "Voulez-vous continuer ?")
        if(reponse == True):
            self.fenetre.destroy()
if __name__ == '__main__':
    fen = Tk()
    man = manuel(1,fen)
    dessin = Canvas(fen, width =200, height =500, bg ="ivory")
    dessin.grid(row = 0, column = 0, rowspan = 2,padx = 5, pady = 5)
    rouge = dessin.create_oval(40,50,137,147, fill = "red")
    jaune = dessin.create_oval(40,177,137,274, fill = "gray")
    vert = dessin.create_oval(40,304,137,401, fill = "gray")
    zone = Frame(fen, bg='#777777')
    zone.grid(row=0,column=1,ipadx=1,ipady = 5)

    btn_next  = Button(zone, text = "Suivant", command = man.suivant)
    btn_next.pack(fill=X)
    btn_prev = Button(zone, text = "Initialiser", command = man.initialiser)
    btn_prev.pack(fill=X)
    btn_quitter = Button(zone, text = "Quitter", command = man.confirm)
    btn_quitter.pack(fill=X)
