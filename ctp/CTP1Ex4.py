
from random import*

argent=5

while argent>0 and argent != 7:
    des=randint(1, 6)

    if des > 4:
        argent=argent+1
        print("+1€")
    else:
        argent=argent-1
        print("-1€")

if argent == 7:
    print("Paul à gagné !")
else:
    print("Paul à perdu tout son argent !")