aux=0
n=int(input("Saisir n val : "))
tab=n*[0]

for i in range(0, n-1):
    tab[i]=int(input("Saisir val "+ str(i) +" du tableau"))
for j in range(0, n-2):
    for i in range(0, n - 2):
        if tab[i] > tab[i+1]:
            aux=tab[i]
            tab[i]=tab[i+1]
            tab[i+1] = aux
for i in range(0, n-1):
    print(tab[i])