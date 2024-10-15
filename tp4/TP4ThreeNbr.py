
a,b,c=int(input("entrez un nombre (a) : ")), int(input("entrez un nombre (b) : ")), int(input("entrez un nombre (c) : "))

if a > b and a > c:
    print("a est le plus grand")
elif b > a and b > c:
    print("b est le plus grand")
else:
    print("c est le plus grand")