from random import*

c=-5

for i in range(1, 9):
    rnd=randint(0,1)
    if rnd==1:
        c=c+1
        print("pile +1€")
    else:
        print("face rien")
print("Ton capital est de : "+str(c))