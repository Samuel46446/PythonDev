# Start of Binary convertor

from math import *

def makeBin(o, puissance) -> int:
    if o==1:
        return puissance
    else:
        return 0

#Ex binary
print("BINARY CONVERTOR : \n")
o0 = int(input("entrez l'octed 0 : "))  #1
o1 = int(input("entrez l'octed 1 : "))  #2
o2 = int(input("entrez l'octed 2 : "))  #4
o3 = int(input("entrez l'octed 3 : "))  #8
o4 = int(input("entrez l'octed 4 : "))  #16
o5 = int(input("entrez l'octed 5 : "))  #32
o6 = int(input("entrez l'octed 6 : "))  #64
o7 = int(input("entrez l'octed 7 : "))  #128
o8 = int(input("entrez l'octed 8 : "))  #256

result=0
result = result + makeBin(o0, 1)
result = result + makeBin(o1, 2)
result = result + makeBin(o2, 4)
result = result + makeBin(o3, 8)
result = result + makeBin(o4, 16)
result = result + makeBin(o5, 32)
result = result + makeBin(o6, 64)
result = result + makeBin(o7, 128)
result = result + makeBin(o8, 256)
print(result)

