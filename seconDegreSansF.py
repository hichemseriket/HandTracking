import math
from cmath import sqrt
import os

a = input("donner a ")
a = int(a)
b = input("donner b ")
b = int(b)
c = input("donner c ")
c= int(c)
d = (b * b) - (4 * a * c)
# d = int(d)
s = -b / (2 * a)
racineDelta = sqrt(d)
s1 = (-b - racineDelta) / (2 * a)
s2 = (-b + racineDelta) / (2 * a)
racineMoinsDelta = sqrt(-d)
z1 = complex(-b / (2 * a), racineMoinsDelta / (2 * a))
z2 = complex(-b / (2 * a), -racineMoinsDelta / (2 * a))
if a != 1:
    print(a, "x² +", b, "x +", c)
elif a == 1:
    print("x² +", b, "x +", c)
if d > 0:
    print("delta est positive et vaut", d, "l'equation admet les deux solution suivant")
    retour = [s1, s2]
    print(s1, s2)
elif (d < 0):
    print("delta est negative et vaut", d, "l'equation n'admet pas de solution reel")
    print("les deux solution imaginaire sont : ")
    retour = [z1, z2]
    print(z1, z2)
else:
    print("delta vaut", d, "l'equation admet une seule solution")
    retour = [s]
    print(s)
