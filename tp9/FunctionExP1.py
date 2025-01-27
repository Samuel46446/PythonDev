def max(L):
    valMax=0
    for i in L:
        if i > valMax:
            valMax = i
    return valMax

l=int(input("saisir la dimension de la liste : "))
liste=[]
for i in range(0, l):
    liste.append(int(input()))
print(liste)
print(max(liste))