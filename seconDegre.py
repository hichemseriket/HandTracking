import math
import os

a = input ( "donner a ")
b = input ( "donner b ")
c = input ( "donner c ")
def solution(a, b, c):
    d = determinant(a, b, c)
    if a != 1:
        print(a, "x² +", b, "x +", c)
    elif a == 1:
        print("x² +", b, "x +", c)
    if d > 0:
        print("delta est positive et vaut", d, "l'equation admet les deux solution suivant")
        racineDelta = math.sqrt(d)
        s1 = (-b - racineDelta) / (2 * a)
        s2 = (-b + racineDelta) / (2 * a)
        retour = [s1, s2]
        print(s1, s2)
    elif (d < 0):
        print("delta est negative et vaut", d, "l'equation n'admet pas de solution reel")
        print("les deux solution imaginaire sont : ")
        racineMoinsDelta = math.sqrt(-d)
        z1 = complex(-b / (2 * a), racineMoinsDelta / (2 * a))
        z2 = complex(-b / (2 * a), -racineMoinsDelta / (2 * a))
        # solutionimaginaire(a, b, c)
        # z1 = solutionimaginaire(a, b, c).z3
        # z2 = solutionimaginaire(a, b, c).z4
        retour = [z1, z2]
        print(z1, z2)
    else:
        print("delta vaut", d, "l'equation admet une seule solution")
        s = -b / (2 * a)
        retour = [s]
        print(s)


def determinant(a, b, c):
    # a = input()
    # b = input()
    # c = input()
    return (b * b) - (4 * a * c)

# os.system("pause")

# solution(a=input(), b=input(), c=input())
solution(2, -2, 1)


def solutionimaginaire(a, b, c):
    d = determinant(a, b, c)
    z3 = complex(-b / (2 * a), math.sqrt(-d) / (2 * a))
    z4 = complex(-b / (2 * a), -math.sqrt(-d) / (2 * a))
    # retour = [z3, z4]
    return z3, z4

    # m = math.pow(i, 2)
    # m = -1

    # je remplace le - de delta par un i²
