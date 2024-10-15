# Start of TP2

from math import *
# Exercice 1
age, taille = int(input("Quel est votre age ? ")), eval(
    input("quel est ta taille ? "))
print("bonjour ", age, " tu mesure ", taille, " mètres")

#Ex temporelle
h = int(input("heure : "))
m = int(input("minute : "))
s = int(input("seconde : "))

htoS = h * 3600
mtoS = m * 60

result = htoS + mtoS + s
print(result)