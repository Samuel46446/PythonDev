
# 1. int et double
# 2. Appliquer la réduction de 10% lorsque le nombre de place acheter et supérieur à 3
# 3. Applique un prix pour un nombre de place et de possiblement appliquer une réduction de 10%
n = int(input("Combien de places de concert souhaitez-vous acheter ? "))
prix = n * 20
if n > 3:
    prix=prix*0.9
print(prix)