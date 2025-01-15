aux=0
n=int(input("Saisir n val : "))
tab=n*[0]
cpt=0
for i in range(0, n):
    tab[i]=int(input("Saisir val "+ str(i) +" du tableau : "))
tab1=[]
j=0
while tab1 != tab:
    tab1=tab
    print("j debut : ", tab)
    for i in range(0, n - 1 - j):
        if tab[i] > tab[i+1]:
            cpt=cpt+1
            aux=tab[i]
            tab[i]=tab[i+1]
            tab[i+1] = aux
            print("i fin : ", tab)
    j=j+1
for i in range(0, n):
    print(tab[i])
print("Nombre de modif : ", cpt)