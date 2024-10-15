
n = int(input("Combien de places de concert souhaitez-vous acheter ? "))
etu = str(input("Êtes vous étudiant ? "))

if etu == "oui":
    isEtu = True
else:
    isEtu = False

prix = n * 20
if isEtu:
    prix=prix*0.75
print(prix)