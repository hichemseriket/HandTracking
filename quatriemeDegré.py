#! /usr/bin/env python
# -*- coding: utf-8 -*-

#     Résolution des équations du quatrième degré
#     de la forme
#     a4 x^4 + a3 x^3 + a2 x^2 + a1 x + a0 = 0

# _________________________________________________________________________________________________________________________________________________________________________
from tkinter import *
from math import *
from cmath import *
from tkinter import messagebox



# _________________________________________________________________________________________________________________________________________________________________________

def resoudre_4_degre():
    global A3, A2, A1, A0
    #    global b,c,d,e
    # considérons l'équation générale du quatrième degré :
    #          a4 x^4 + a3 x^3 + a2 x^2 + a1 x + a0 = 0   (1)
    # entrée des coefficients a4 , a3 , a2 , a1 , a0
    a4, a3, a2, a1, a0 = float(entr4.get()), float(entr3.get()), float(entr2.get()), float(entr1.get()), float(
        entr0.get())
    # transformation de l'équation :
    #          x^4 + b x^3 + c x^2 + d x + e = 0   (2)
    # avec les coefficients :
    b, c, d, e = a3 / a4, a2 / a4, a1 / a4, a0 / a4
    # après le changement de variable : x = X - b/4
    # l'équation (2) devient :
    #          X^4 + p X^2 + q X + r = 0   (3)
    # avec les coefficients :
    p, q, r = c - 3. / 8 * b ** 2, d - b * c / 2 + b ** 3 / 8, e - b * d / 4 + c * b ** 2 / 16 - 3. / 256 * b ** 4
    # étudions l'expression suivante :
    #          X^4 + y X^2 + y^2/4
    # soit :
    #          ( X^2 + y/2 )^2 = -p X^2 - q X - r + y X^2 + y^2/4
    #          ( X^2 + y/2 )^2 = ( y - p ) X^2 - q X + y^2/4 - r
    # son second membre est un carré parfait si le discriminant  de l'équation du second degré en X est nul :
    #          q^2 - 4 (y - p ) ( y^2 /4 - r ) = 0
    #          y^3 -p y^2 - 4 r y + 4 p r - q^2 = 0
    # considérons maintenant l'équation suivante :
    #          A3 y^3 + A2 y^2 + A1 y + A0 = 0
    # avec les coefficients :
    A3, A2, A1, A0 = 1, -p, -4 * r, 4 * p * r - q ** 2
    #  et recherchons une racine réelle y1 :
    resoudre_3_degre()
    if y1 == p:
        X1, X2, X3, X4 = sqrt(-p / 2 + 1. / 2 * sqrt(p ** 2 - 4 * r)), sqrt(
            -p / 2 - 1. / 2 * sqrt(p ** 2 - 4 * r)), -sqrt(-p / 2 + 1. / 2 * sqrt(p ** 2 - 4 * r)), -sqrt(
            -p / 2 - 1. / 2 * sqrt(p ** 2 - 4 * r))
    else:
        y0 = y1
        #  Discriminant D12
        D12 = -y0 - p + 2 * q / sqrt(y0 - p)
        #  Discriminant D34
        D34 = -y0 - p - 2 * q / sqrt(y0 - p)
        # calcul des quatre racines complexes de l'équation : X1, X2, X3, X4
        X1, X2, X3, X4 = 1. / 2 * (-sqrt(y0 - p) + sqrt(D12)), 1. / 2 * (-sqrt(y0 - p) - sqrt(D12)), 1. / 2 * (
                sqrt(y0 - p) + sqrt(D34)), 1. / 2 * (sqrt(y0 - p) - sqrt(D34))
    # calcul des quatre racines complexes de l'équation : x1, x2, x3, x4
    x1, x2, x3, x4 = X1 - b / 4, X2 - b / 4, X3 - b / 4, X4 - b / 4
    # isolation des parties réelles et imaginaires des quatre racines x1, x2, x3, x4
    xr1, xi1 = x1.real, x1.imag
    xr2, xi2 = x2.real, x2.imag
    xr3, xi3 = x3.real, x3.imag
    xr4, xi4 = x4.real, x4.imag
    # affichage des parties réelles et imaginaires avec trois décimales
    x1, x2, x3, x4 = complex(round(xr1, 3), round(xi1, 3)), complex(round(xr2, 3), round(xi2, 3)), complex(
        round(xr3, 3), round(xi3, 3)), complex(round(xr4, 3), round(xi4, 3))
    # affichage des quatre racines dans le plan complexe de la fenêtre
    can.coords(c1, L / 2 + 50 * xr1 - R, L / 2 - 50 * xi1 - R, L / 2 + 50 * xr1 + R, L / 2 - 50 * xi1 + R)
    can.coords(c2, L / 2 + 50 * xr2 - R, L / 2 - 50 * xi2 - R, L / 2 + 50 * xr2 + R, L / 2 - 50 * xi2 + R)
    can.coords(c3, L / 2 + 50 * xr3 - R, L / 2 - 50 * xi3 - R, L / 2 + 50 * xr3 + R, L / 2 - 50 * xi3 + R)
    can.coords(c4, L / 2 + 50 * xr4 - R, L / 2 - 50 * xi4 - R, L / 2 + 50 * xr4 + R, L / 2 - 50 * xi4 + R)
    # affichage de leur légende dans le plan complexe de la fenêtre
    can.coords(txt_x1, L / 2 + 50 * xr1 + 15, L / 2 - 50 * xi1)
    can.coords(txt_x2, L / 2 + 50 * xr2, L / 2 - 50 * xi2 - 15)
    can.coords(txt_x3, L / 2 + 50 * xr3, L / 2 - 50 * xi3 + 15)
    can.coords(txt_x4, L / 2 + 50 * xr4 - 15, L / 2 - 50 * xi4)

    txta.configure(text="" + str(a4))
    txtb.configure(text="" + str(a3))
    txtc.configure(text="" + str(a2))
    txtd.configure(text="" + str(a1))
    txte.configure(text="" + str(a0))

    text_x1.configure(text="" + str(x1))
    text_x2.configure(text="" + str(x2))
    text_x3.configure(text="" + str(x3))
    text_x4.configure(text="" + str(x4))


# _________________________________________________________________________________________________________________________________________________________________________

def resoudre_3_degre():
    global y1, y2, y3
    # considérons l'équation générale du troisième degré :
    #          A3 y^3 + A2 y^2 + A1 y + A0 = 0   (1)
    # soit encore :
    #          A y^3 + B y^2 + C y + D = 0   (2)
    # avec :
    B, C, D = A2 / A3, A1 / A3, A0 / A3
    #  après le changement de variable y = Y - B/3
    # et en posant :
    P, Q = C / 3 - B * B / 9, B * B * B / 27 - B * C / 6 + D / 2
    # l'équation (2) devient :
    #          Y^3 + 3PY + 2Q = 0
    # calcul du discriminant
    Discriminant = P ** 3 + Q ** 2
    # calcul de s = (signe de Q) x sqrt(valeur absolue de P)
    if P != 0: s = Q / fabs(Q) * sqrt(fabs(P))
    # calcul des trois racines complexes de l'équation : Y1, Y2, Y3
    if P < 0:
        if Discriminant <= 0:
            f = acos(Q / (s ** 3))
            Y1 = complex(-2 * s * cos(f / 3))
            Y2 = complex(2 * s * cos(60 * pi / 180 - f / 3))
            Y3 = complex(2 * s * cos(60 * pi / 180 + f / 3))
        if Discriminant > 0:
            fc = acosh(Q / (s ** 3))
            Y1 = complex(-2 * s * cosh(fc / 3))
            Y2 = complex(s * cosh(fc / 3), sqrt(3) * s * sinh(fc / 3))
            Y3 = complex(s * cosh(fc / 3), -sqrt(3) * s * sinh(fc / 3))
    if P > 0:
        fs = asinh(Q / (s ** 3))
        Y1 = complex(-2 * s * sinh(fs / 3))
        Y2 = complex(s * sinh(fs / 3), sqrt(3) * s * cosh(fs / 3))
        Y3 = complex(s * sinh(fs / 3), -sqrt(3) * s * cosh(fs / 3))
    if P == 0:
        if Q > 0: Y1 = Y2 = Y3 = complex(pow(2 * Q, 1. / 3))
        if Q < 0: Y1 = Y2 = Y3 = complex(pow(-2 * Q, 1. / 3))
        if Q == 0: Y1 = Y2 = Y3 = complex(0)
    # calcul des trois racines complexes de l'équation : y1, y2, y3
    y1, y2, y3 = Y1 - A2 / (3 * A3), Y2 - A2 / (3 * A3), Y3 - A2 / (3 * A3)


# _________________________________________________________________________________________________________________________________________________________________________

def presentation():
    "Fenêtre-message contenant la description sommaire de la méthode de calcul"
    msg = Toplevel()
    Message(msg, bg="dark green", fg="white", width=810, font="Arial 9",
            text='''Méthode de calcul\n La méthode choisie est assez originale, puisqu'elle fait appel aux 
            trigonoméries rectiligne et hyperbolique et à la représentation complexe des racines. Le code a pour 
            objet la résolution des équations du quatrième degré de la forme : a4 x^4 + a3 x^3 + a2 x^2 + a1 x + a0 = 
            0   (1) 

Nota : pour résoudre les équations de degré inférieur, il suffit de choisir la valeur zéro pour les derniers coefficients :
        - troisième degré : a0 = 0
        - second degré : a1 , a0 = 0, 0
        - premier degré : a2 , a1 , a0 = 0 , 0 , 0
et d'éliminer les racines nulles

Après avoir ramené l'équation (1) sous la forme suivante :
          x^4 + b x^3 + c x^2 + d x + e = 0   (2)
avec les nouveaux coefficients :
          b , c , d , e = a3 / a4 , a2 / a4 , a1 / a4 , a0 / a4
Aaprès le changement de variable : x = X - b/4
l'équation (2) devient :
          X^4 + p X^2 + q X + r = 0   (3)
avec les coefficients :
          p ,q ,r = c - 3./8 b^2 ,d - b c / 2 + b^3 / 8 ,e - b d / 4 + c b^2 / 16 - 3 / 256 b^4  
Etudions maintenant l'expression suivante :
          X^4 + y X^2 + y^2 / 4
Elle s'écrit aussi :
          ( X^2 + y/2 )^2 = - p X^2 - q X - r + y X^2 + y^2 / 4
          ( X^2 + y/2 )^2 = ( y - p ) X^2 - q X + y^2 / 4 - r
Son second membre est un carré parfait si le discriminant  de l'équation du second degré en X est nul :
          q^2 - 4 (y - p ) ( y^2 / 4 - r ) = 0
          y^3 - p y^2 - 4 r y + 4 p r - q^2 = 0

Considérons alors l'équation suivante :
          A3 y^3 + A2 y^2 + A1 y + A0 = 0   (3)
avec les coefficients :
          A3 ,A2 ,A1 ,A0 = 1, -p , -4 r , 4 p r - q^2
et recherchons une racine réelle y1 de (3) :
L'équation (3) s'écrit :
          y^3 + B y^2 + C y + D =0   (4)
avec les nouveaux coefficients :
          B, C, D = A2 / A3, A1 / A3,A0 / A3
Après le changement de variable y = Y - B / 3
et en posant :
          P , Q = C/3 - B^2 / 9, B^3 / 27 - B C / 6 + D / 2
l'équation (4) devient :
          Y^3 + 3 P Y + 2 Q = 0   (5)
calcul du discriminant
          Discriminant = P^3 + Q^2
on procède ensuite au calcul des trois racines complexes Y1, Y2, Y3 de l'équation (5)
puis à celui des trois racines complexes y1, y2, y3 de l'équation (4)
ce qui permet de déterminer la racine recherchée ci-dessus : y1

On revient alors au calcul de X en résolvant les équations du second degré suivantes :
          ( X^2 + y/2 )^2 = ( y1 - p ) ( X - q / 2 ( y1 - p ) )^2
          X^2 +/- sqrt ( y1- p ) X  -/+ q / 2 / sqrt ( y1 - p ) + y1 / 2 = 0
ce qui donne X1, X2, X3, X4 puis x1, x2, x3, x4''').pack(padx=10, pady=10)


# _________________________________________________________________________________________________________________________________________________________________________

def processus():
    "Fenêtre-message contenant la description du processus"
    msg = Toplevel()
    Message(msg, bg="dark green", fg="white", width=500, font="Arial 9",
            text='''PROCESSUS à suivre\n
        1. Entrer la valeur des 4 coefficients a4, a3, a2, a1, a0
            Nota : lorsqu'un coefficient est nul, il est nécessaire d'entrer 0 dans  le champ
        2. Cliquer sur le bouton < Résoudre ! > :
        3. Les 4 racines de l'équation apparaissent sous la forme suivante :
            racine x = partie réelle + partie imaginaire x  j
            ainsi que dans le plan complexe :
                parties réelles en abcisse
                parties imaginaires en ordonnée
        5. Cliquer sur < Quitter le jeu !> pour abandonner la partie\n''').pack(padx=10, pady=10)


# _________________________________________________________________________________________________________________________________________________________________________

def aPropos():
    "Fenêtre-message indiquant les versions utilisées"
    msg = Toplevel()
    Message(msg, width=200, aspect=100, justify=CENTER,
            text='''Résolution des équations du quatrième degré 
        HCD, Novembre 2006
        Python version 2.5
        Tk version 8.4''').pack(padx=10, pady=10)


# _________________________________________________________________________________________________________________________________________________________________________

def quitter():
    " pour quitter l'application "
    ans = messagebox.showinfo('Résolution des équations du troisième degré', "Voulez-vous réellement quitter ?")
    if ans: root.quit()


# _________________________________________________________________________________________________________________________________________________________________________

def makemenu(win):
    "barre de menu"
    top = Menu(win)
    win.config(menu=top)
    R = Menu(top)
    top.add_cascade(label='Présentation', menu=R, underline=0)
    R.add_command(label='Méthode de calcul', command=presentation, underline=0)
    R.add_command(label='Processus', command=processus, underline=0)
    R.add_command(label='A propos', command=aPropos, underline=0)
    Q = Menu(top)
    top.add_cascade(label='Quitter !', menu=Q, underline=0)
    Q.add_command(label='Quitter le jeu !!', command=quitter, underline=0)


# _________________________________________________________________________________________________________________________________________________________________________

# Programme Principal
root = Tk()
root.title("Résolution des équations du quatrième degré")
root.geometry('800x800')
L = 500
R = 8
makemenu(root)

# _________________________________________________________________________________________________________________________________________________________________________

can = Canvas(root, bg='dark green', height=L, width=L)
can.grid(row=10, column=0)
can.create_line(0, L / 2, L, L / 2, fill='orange')
can.create_line(L / 2, 0, L / 2, L, fill='orange')
c1 = can.create_oval(0, 0, 0, 0, fill='red', width=1)
c2 = can.create_oval(0, 0, 0, 0, fill='red', width=1)
c3 = can.create_oval(0, 0, 0, 0, fill='red', width=1)
c4 = can.create_oval(0, 0, 0, 0, fill='red', width=1)
(Label(root,
       text="Equation du quatrième degré dont on cherche les racines x1,x2,x3,x4 dans le plan complexe :\na4 x^4 + a3 x^3 + a2 x^2 + a1 x + a0 = 0\nx1,2,3,4= (partie réelle de x1,2,3,4 + partie imaginaire de x1,2,3,4 x j)")).grid(
    row=0, column=0)

# Entrées
entr4 = Entry(root)
entr4.grid(row=1, column=1)
entr3 = Entry(root)
entr3.grid(row=2, column=1)
entr2 = Entry(root)
entr2.grid(row=3, column=1)
entr1 = Entry(root)
entr1.grid(row=4, column=1)
entr0 = Entry(root)
entr0.grid(row=5, column=1)

(Label(root, text="entrée du coefficient a4 =")).grid(row=1, column=0, sticky=E)
txta = Label(root)
(Label(root, text="entrée du coefficient a3 =")).grid(row=2, column=0, sticky=E)
txtb = Label(root)
(Label(root, text="entrée du coefficient a2 =")).grid(row=3, column=0, sticky=E)
txtc = Label(root)
(Label(root, text="entrée du coefficient a1 =")).grid(row=4, column=0, sticky=E)
txtd = Label(root)
(Label(root, text="entrée du coefficient a0 =")).grid(row=5, column=0, sticky=E)
txte = Label(root)

(Label(root, text="racine x1 =")).grid(row=6, column=0, sticky=E)
text_x1 = Label(root)
text_x1.grid(row=6, column=1)
(Label(root, text="racine x2 =")).grid(row=7, column=0, sticky=E)
text_x2 = Label(root)
text_x2.grid(row=7, column=1)
(Label(root, text="racine x3 =")).grid(row=8, column=0, sticky=E)
text_x3 = Label(root)
text_x3.grid(row=8, column=1)
(Label(root, text="racine x4 =")).grid(row=9, column=0, sticky=E)
text_x4 = Label(root)
text_x4.grid(row=9, column=1)

can.create_text(L - 30, L / 2 - 10, text='axe réel', fill="white")
can.create_text(L / 2 + 40, 10, text='axe imaginaire', fill="white")
can.create_text(L - 10, L / 2 + 10, text='5', fill="white")
can.create_text(10, L / 2 + 10, text='-5', fill="white")
can.create_text(L / 2 - 10, L / 2 + 10, text='0', fill="white")
can.create_text(L / 2 - 10, 10, text='5', fill="white")
can.create_text(L / 2 - 10, L - 10, text='-5', fill="white")
txt_x1 = can.create_text(-10, 0, text='x1', fill="yellow")
txt_x2 = can.create_text(-10, 0, text='x2', fill="yellow")
txt_x3 = can.create_text(-10, 0, text='x3', fill="yellow")
txt_x4 = can.create_text(-10, 0, text='x4', fill="yellow")

button = Button(root, text='Résoudre !', command=resoudre_4_degre)
button.grid(row=6, column=0)

root.mainloop()
root.destroy()
