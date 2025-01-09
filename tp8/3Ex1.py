from random import *

listLaunch=[]
sumLaunch=0
gain=0

for i in range(10):
    rnd = randint(1,6)
    listLaunch.append(rnd)
    sumLaunch=sumLaunch+rnd

    if rnd % 2 == 0:
        gain=gain+1
    else:
        gain=gain-1

    if listLaunch[i] == listLaunch[i-1]:
        gain=gain+5

if sumLaunch > 10:
    gain=gain+3

print("Somme : ", sumLaunch)
print("Tab : ", listLaunch)
print("Gain : ", gain)