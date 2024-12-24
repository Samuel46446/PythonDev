dim=int(input("saisir la dimension de la liste : "))
liste=dim*["0"]

for i in range(0, dim):
    liste[i]=input("Saisir : ")

print(liste)