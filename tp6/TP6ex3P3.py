from random import*

#Devinette

choixNbrOrdi=randint(1,100)
repPlayer=0

if 1 <= choixNbrOrdi <= 100:
    while repPlayer != choixNbrOrdi:
        repPlayer=int(input("J'ai choisie un nombre entre 1 et 100, essaye de le trouver : "))
        if repPlayer > choixNbrOrdi:
            print("Plus petit")
        elif repPlayer < choixNbrOrdi:
            print("Plus grand")
print("Bravo le nombre secret était ", choixNbrOrdi)