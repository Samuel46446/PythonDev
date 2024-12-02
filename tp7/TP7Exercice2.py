#III Ex 2
from typing import final

def dom(nb : int, phrase : str, phrase2 : str):
    if int(code[7]) == nb:
        return phrase2
    return phrase

nom=input("Saisissez votre nom : ")
prenom=input("Saisissez votre prenom : ")
code=""
#Result Var
emploie=""
sexe=""
Pronom=""
numEnbch=""
anneeEnbch=""

while len(code) < 8:
    code=str(input("Saisissez votre code personnel : "))
    if len(code) == 8:
        print("bravo")
    else:
        print("erreur veuillez recommencer")

emploie = dom(0, emploie, "de la direction")
emploie = dom(1, emploie, "du secrétariat")
emploie = dom(2, emploie, "de la gestion")
emploie = dom(3, emploie, "informatique")
emploie = dom(4, emploie, "de la communication")
emploie = dom(5, emploie, "de l'entretien")
emploie = dom(6, emploie, "de la fabrication")

if int(code[7]) > 6 or int(code[7]) < 0:
    emploie="secret"

if int(code[6]) == 1:
    sexe="Madame"
    Pronom="Elle"
elif int(code[6]) == 0:
    sexe="Monsieur"
    Pronom="Il"
else:
    sexe="Unknow"
    Pronom="Ey"

numEnbch=code[2]+code[3]+code[4]+code[5]

yearMax="2024" #24
yearMin="1925" #25

if int(str(code[0]+code[1])) >= 25:
    anneeEnbch="19"+str(code[0]+code[1])
elif int(str(code[0]+code[1])) <= 24:
    anneeEnbch="20"+str(code[0]+code[1])
else:
    anneeEnbch="9999"

finalString=sexe+" "+prenom+" "+nom+" travaille au service "+emploie+". "+Pronom+" travaille dans l'entreprise depuis "+anneeEnbch+" et son numéro d'embauche est le "+numEnbch+"."
print(finalString)