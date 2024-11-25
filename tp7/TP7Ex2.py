mot=input("écris un mot : ")
l=len(mot)
nouveaumot=""
if l%2 == 0:
    for i in range(0, l-1, 2):
        nouveaumot=nouveaumot+mot[i:i+2]+"#"
else:
    for i in range(0, l-1, 2):
        nouveaumot=nouveaumot+mot[i:i+2]+"#"
    nouveaumot=nouveaumot+mot[l-1]
print(nouveaumot)