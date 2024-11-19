
#Nombres premiers

nbr=0

while nbr != 0 and nbr >=100:
    nbr = int(input("Entrez un nombre pour savoir s'il est premier : "))

if (nbr >= 1 and nbr%nbr <= 0 and nbr%1 <= 0) or nbr == 2:
    print("Votre nombre est premier !")
else:
    print("Votre nombre n'est pas premier !")

