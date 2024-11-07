#Euclide
a=int(input("Saisissez le 1er entier pgcd : "))
b=int(input("Saisissez le 2e entier pgcd : "))

r=b #init pour que la boucle se déclenche

while a%b > 0:
    r=a%b
    a=b
    b=r
print("Le pgcd est : ", r)
