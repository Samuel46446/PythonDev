montant = int(input("Saissisez un montant en (€) : "))

nbrBilletde50=0
isRun=True
while isRun:
    montant = montant - 50
    if montant < 0:
        isRun=False
    elif montant == 0:
        nbrBilletde50=nbrBilletde50+1
    else:
        nbrBilletde50=nbrBilletde50+1

print(nbrBilletde50)
nbrBilletde20=0
isRun=True
while isRun:
    montant = montant - 20
    if montant < 0:
        isRun=False
    elif montant == 0:
        nbrBilletde20=nbrBilletde20+1
    else:
        nbrBilletde20=nbrBilletde20+1

print(nbrBilletde20)

nbrBilletde10=0
isRun=True
while isRun:
    montant = montant - 10
    if montant < 0:
        isRun=False
    elif montant == 0:
        nbrBilletde10=nbrBilletde10+1
    else:
        nbrBilletde10=nbrBilletde10+1

print(nbrBilletde10)

nbrBilletde5=0
nbrPiecede2e=0
nbrPiecede1e=0
nbrPiecede50c=0
nbrPiecede20c=0
nbrPiecede10c=0
nbrPiecede5c=0
nbrPiecede2c=0
nbrPiecede1c=0

#Correction
a=eval(input("montant : "))
b=a//50
c=a%50
print("le nombre de billets de 50 et de ", b, " et le reste est ", c)
d=c//20
e=d%20
print("le nombre de billets de 20 et de ", d, " et le reste est ", e)