from random import*

#Devinette

choixNbrOrdi=randint(1,100)
repPlayer=0
nbTentative=0

if 1 <= choixNbrOrdi <= 100:
    while repPlayer != choixNbrOrdi:
        repPlayer=int(input("J'ai choisie un nombre entre 1 et 100, essaye de le trouver : "))
        if repPlayer > choixNbrOrdi:
            print("Plus petit")
            nbTentative += 1
        elif repPlayer < choixNbrOrdi:
            print("Plus grand")
            nbTentative += 1
print("Bravo le nombre secret était ", choixNbrOrdi)
print("Tu as réussis en ", nbTentative, " tentatives")