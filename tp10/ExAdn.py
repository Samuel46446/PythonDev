def comp(car):
    if car == 'A':
        return 'T'
    elif car == 'G':
        return 'C'
    elif car == 'C':
        return 'G'
    else:
        return 'A'

def mystery(brin1, brin2):
    if len(brin1) != len(brin2):
        B=False
    else:
        B=True
        for i in range(len(brin1)):
            if brin1[i] != comp(brin2[i]):
                B=False
    return B

def plusPres(brin1):
    a, t, c, g = 0
    for i in range(len(brin1)):
        if brin1[i] == 'A':
            a=a+1
        elif brin1[i] == 'T':
            t=t+1
        elif brin1[i] == 'C':
            c=c+1
        else:
            g=g+1
    max = 0
    id=-1
    tab = [a,t,c,g]
    tab2 = ['A', 'T', 'C', 'G']
    for i in range(len(tab)):
        if tab[i] > max:
            id=i
            max=tab[i]
    return tab2[id]

def longA(brin1):
    chaineA = 0
    tempA = 0
    for i in range(len(brin1)):
        if brin1[i] == 'A':
            tempA
        else:
            if chaineA == 0:
                ch

            if tempA > chaineA:
                chaineA = tempA
                tempA = 0