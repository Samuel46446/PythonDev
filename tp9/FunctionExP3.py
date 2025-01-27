import sys

def max(L):
    valMax=0
    for i in L:
        if i > valMax:
            valMax = i
    return valMax

def min(L):
    valMin=int(sys.maxsize)
    for i in L:
        if i < valMin:
            valMin = i
    return valMin

def extends(L):
    return max(L) - min(L)

l=int(input("saisir la dimension de la liste : "))
liste=[]
for i in range(0, l):
    liste.append(int(input()))
print(liste)
print(min(liste))
print(max(liste))
print(extends(liste))