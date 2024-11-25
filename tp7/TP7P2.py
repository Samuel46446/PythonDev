phrase=input("écris une phrase sans ponctuation : ")
l=len(phrase)
c=1
for i in range(0,l):
    if phrase[i] == " ":
        c=c+1
print(c)
print(l)