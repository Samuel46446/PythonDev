n=int(input("saisir un entier : "))
binaire=""
q=n
while q%2 == 0:
    q=q//2
    binaire=str(q%2)+binaire
print(binaire)