#1
km=30
jours=21
for i in range(1, jours+1):
    if i != 1:
        km=km+10

    if i == 10:
        print("Nombre de km 10e jour : "+str(km))

    sem=i%7
    if sem==0:
        print("Nombre de km de la semaine : "+str(km))
print("Nombre total de km : "+str(km))