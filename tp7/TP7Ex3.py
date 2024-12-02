n=int(input("saisir un entier : "))
binaire=""
q=n
if q == 0:
    binaire=0
else:
    while q != 0:
        binaire=str(q%2)+binaire
        q=q//2
print(binaire)