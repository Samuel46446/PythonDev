
age=int(input("quelle age pour la voiture : "))
km=int(input("combien de km au compteur : "))
if age>=20 and km >= 300000:
    print("il est temps de changer de voiture")
elif age>=10 or km>=180000:
    print("il est temps de changer la courroie de distribution")
else:
    print("il est temps de changer de voiture")