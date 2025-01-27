def min(L):
    valMin=L[0]
    for i in L:
        if i < valMin:
            valMin = i
    return valMin

l=int(input("saisir la dimension de la liste : "))
liste=[]
for i in range(0, l):
    liste.append(int(input()))
print(liste)
print(min(liste))