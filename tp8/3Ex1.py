from random import *

listLaunch=[]
sumLaunch=0

for i in range(10):
    rnd = randint(1,6)
    listLaunch.append(rnd)
    sumLaunch=sumLaunch+rnd
print("Somme : ", sumLaunch)
print("Tab : ", listLaunch)