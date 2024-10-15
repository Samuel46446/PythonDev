n = int(input("Combien de places de concert souhaitez-vous acheter ? "))
etu = str(input("Êtes vous étudiant ? "))
date = str(input("Saissisez le mois ? "))

if etu == "oui":
    isEtu = True
else:
    isEtu = False

if date == "juin":
    prix = n * 16
    if isEtu:
        prix = prix * 0.75
else:
    prix = n * 20
    if n > 3:
        prix=prix*0.9

print(prix)