
n=int(input("saisir un nombre entier"))
for i in range(1,n):
    print(i)
print("ce sont les nombres entiers inférieurs à n ?")

n=int(input("saisir un nombre entier"))
for i in range(1,n+1):
    print(i)
print("entier de 1 à n ?")

n=int(input("saisir un nombre entier"))
for i in range(1,n+1,2):
    print(i)
print("ce sont les nombres impairs inférieurs à n")

a=int(input("saisir un nombre entier inférieur à 255"))
for i in range(1, 10):
    print(int(a%2))
    a=int(a/2)
print("l'octet correspondant est cette série de bits lue à l'envers.")