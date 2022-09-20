from tkinter import *
from tkinter import messagebox
from version1 import *
import time
class version2:
    def __init__(self,fenetre):
        self.fenetre = fenetre
        
    def manuel2(self):
        manuel(1,self.fenetre)
        
    def auto(self):
        btn_man.pack_forget()
        btn_auto.pack_forget()
        l1.pack(fill = X)
        sc.pack(fill=X)
        l2.pack(fill = X)
        while True:
            dessin.itemconfigure(rouge, fill = "red")
            dessin.itemconfigure(jaune, fill = "gray")
            dessin.itemconfigure(vert, fill = "gray")
            time.sleep(1)
            dessin.itemconfigure(jaune, fill = "yellow")
            dessin.itemconfigure(rouge, fill = "gray")
            dessin.itemconfigure(vert, fill = "gray")
            time.sleep(1)
            dessin.itemconfigure(vert, fill = "green")
            dessin.itemconfigure(rouge, fill = "gray")
            dessin.itemconfigure(jaune, fill = "gray")
            time.sleep(1)

        
    def change_vitesse(self,v):
        vitesse = int(v)
        while True:
            dessin.itemconfigure(rouge, fill = "red")
            dessin.itemconfigure(jaune, fill = "gray")
            dessin.itemconfigure(vert, fill = "gray")
            time.sleep(vitesse)
            dessin.itemconfigure(jaune, fill = "yellow")
            dessin.itemconfigure(rouge, fill = "gray")
            dessin.itemconfigure(vert, fill = "gray")
            time.sleep(vitesse)
            dessin.itemconfigure(vert, fill = "green")
            dessin.itemconfigure(rouge, fill = "gray")
            dessin.itemconfigure(jaune, fill = "gray")
            time.sleep(vitesse)
            

if __name__ == '__main__':
    fen  = Tk()
    v = IntVar()
    v2 = IntVar()
    vers = version2(fen)
    dessin = Canvas(fen, width =200, height =500, bg ="ivory")
    dessin.grid(row = 0, column = 0, rowspan = 2,padx = 5, pady = 5)
    rouge = dessin.create_oval(40,50,137,147, fill = "red")
    jaune = dessin.create_oval(40,177,137,274, fill = "gray")
    vert = dessin.create_oval(40,304,137,401, fill = "gray")
    zone = Frame(fen, bg='#777777')
    zone.grid(row=0,column=1,ipadx=5,ipady = 5)
    btn_man  = Radiobutton(zone, text = "Manuel", variable = v, command = vers.manuel2, value = 1)
    btn_man.pack(fill=X)
    btn_auto = Radiobutton(zone, text = "Automatique", variable = v, command = vers.auto, value = 2)
    btn_auto.pack(fill=X)
    l1 = Label(zone, text = "rapide")
    l1.pack_forget()
    sc = Scale( zone, variable = v2,
           from_ = 100, to = 1,
           orient = VERTICAL)
    sc.pack_forget()
    sc.bind('<Button-1>', vers.change_vitesse(str(v2)))
    l2 = Label(zone, text = "lent")
    l2.pack_forget()
