
a,b=int(input("saisir nbr (a) : ")), int(input("saisir nbr entier (b) : "))

if b!=a:
    print("les nombres sont différents")
if a<b:
    print("le plus grand est b")
elif b<a:
    print("le plus grand est a")
else:
    print("les valeurs sont égales")