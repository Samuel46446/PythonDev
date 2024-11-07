#Mot de passe

mdp="sesame"
inputMdp=""
erreurCpt=3

while inputMdp != mdp and erreurCpt > 0:
    inputMdp=str(input("Saisissez votre mot de passe : "))
    if inputMdp != mdp:
        erreurCpt-=1

if inputMdp == mdp:
    print("Bienvenue a Python World !")
else:
    print("Erreur nous n'avons pas pu vous reconnaitre jeune serpent !")