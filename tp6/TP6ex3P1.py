from random import*

#ruine du joueur

playerCoins=5

while playerCoins > 0:
    delay=str(input("Appuyer sur entrer pour continuer !"))
    rnd=randint(0,1)
    if rnd==1:
        playerCoins+=1
        print("pile +1€")
    else:
        playerCoins-=1
        print("face rien")
    print("Ton capital est de : ", playerCoins)
print("Vous avez tout perdu !")