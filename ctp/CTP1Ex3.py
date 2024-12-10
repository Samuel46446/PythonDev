
n=int(input("Donner un nombre entier : "))
c=0

for i in range(1, n+1):
    if n%i==0:
        print(i)
        c=c+1
if c==2:
    print("oui")
else:
    print("non")