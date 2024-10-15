from random import*

def randDee():
    return randint(1,6)

points=10

while points > 0:
    somme=0
    for i in range(10):
        somme=somme+randDee()
    print("La somme des 10 lancer de dés est de : "+str(somme))
    if somme%2 == 0:
        points=points+1
        print("Vous gagnez 1 point")
    else:
        points = points - 2
    print("Vous possédez : " + str(points) + " points !")
    start=str(input("Appuyez sur entrer pour une nouvelle partie"))
print("perdu")