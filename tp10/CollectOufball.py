from random import *

def sum(L):
    for i in range(len(L)):
        print(i, " : ", L[i])

M=[0]*11

for i in range(100):
    j = randint(0, 10)
    M[j] = M[j] + 1

sum(M)