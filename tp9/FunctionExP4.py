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

l=int(input("saisir la dimension de la liste1 : "))
liste1=[]
for i in range(0, l):
    liste1.append(int(input()))
print(liste1)
print(min(liste1))
print(max(liste1))
print(extends(liste1))

ll=int(input("saisir la dimension de la liste2 : "))
liste2=[]
for i in range(0, ll):
    liste2.append(int(input()))
print(liste2)
print(min(liste2))
print(max(liste2))
print(extends(liste2))

print(extends(liste1) - extends(liste2))
