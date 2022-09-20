#!/usr/bin/env python

# -*- coding: utf-8 -*-

from tkinter import *


from tkinter import *

from PIL import Image as Img

from PIL import ImageTk


# - - - - - - - - - - - - - -

# Définitions des fonctions utilisées

# - - - - - - - - - - - - - -


def activation(event) :

    print ("Vous avez cliqué sur ", event.widget)

    print ("Les coordonnées locales sont : ")

    # On affiche les coordonnées de l'événement, contenues dans x et y

    print(event.x)

    print(event.y)

    print ("Les coordonnées globales sont : ")

    # On affiche les coordonnées de l'événement avec x_root et y_root

    print(event.x_root)

    print(event.y_root)

    try:

        widgetClique = event.widget

        nouvelle_temp = Img.new("RGB", (40,40), (255,255,0))

        nouvelleTk_temp = ImageTk.PhotoImage(nouvelle_temp)

        widgetClique.configure(image = nouvelleTk_temp)

        # la ligne suivante évite au ramasse-miette de détruire nouvelleTk_temp car

        # cette variable n'est sinon plus pointée par une variable du corps du programme.

        # Sans cette ligne, nouvelleTk_temp serait inexistante hors de la fonction

        widgetClique.monEmplacement = nouvelleTk_temp

    except:

        print("On clique directement sur la fenêtre")


# - - - - - - - - - - - - - -

# Création de la fenêtre et des objets associés la fenêtre

# - - - - - - - - - - - - - -


fen_princ = Tk()


# Création d'un Label nommé monAffichage

monAffichage = Label(fen_princ, text="Belles images variables en cliquant", width=70)

monAffichage.pack()


# Création des images de base


presentation = Img.new("RGB", (40,40), (0,0,255))

presentationTk = ImageTk.PhotoImage(presentation)

presentation2 = Img.new("RGB", (40,40), (0,0,255))

presentationTk2 = ImageTk.PhotoImage(presentation2)

presentation3 = Img.new("RGB", (40,40), (0,0,255))

presentationTk3 = ImageTk.PhotoImage(presentation3)


# Création des labels de type image associés aux presentationTk


carre1 = Label(fen_princ, image=presentationTk)

carre1.pack()


carre2 = Label(fen_princ, image=presentationTk2)

carre2.pack()


carre3 = Label(fen_princ, image=presentationTk3)

carre3.pack()


# - - - - - - - - - - - - - -

# Bouclage de la fenêtre fen_princ

# - - - - - - - - - - - - - -

fen_princ.bind('<Button-1>', activation )

fen_princ.mainloop()
